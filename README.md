# Fine-tuning Mistral 7B on MIMIC4 Biomedical Data with Single GPU and QLoRA

This guide outlines the steps to specialize any language model for a particular task easily. With Modal, streamline your training process in the cloud, avoiding the hassle of managing infrastructure, such as building images and configuring GPUs.

We demonstrate training [Mistral 7B](https://huggingface.co/mistralai/Mistral-7B-v0.1) on a single GPU via [QLoRA](https://github.com/artidoro/qlora), a fine-tuning method that merges quantization with LoRA to efficiently reduce memory consumption while maintaining performance. Our model undergoes 4-bit quantization and is trained on [MIMIC4 biomedical data](https://physionet.org/content/mimiciii/), adapting it for healthcare applications. Modal facilitates the process with its [GPU-accelerated setup](https://modal.com/docs/guide/gpu) and [integrated storage solution](https://modal.com/docs/guide/volumes), allowing for quick training initiation.

Customizing this setup for various needs is straightforward:
- Change the `BASE_MODEL` in `common.py` to fine-tune a different language model.
- For personal training data (stored as local .csv or .jsonl files), upload your datasets to modal.Volume with `modal volume put training-data-vol /local_path/to/dataset /training_data`, adjusting prompt templates to suit your data.
- Adjust or remove quantization by modifying `BitsandBytesConfig` in `train.py`, ensuring to replicate changes in `inference.py`.

## Before Starting - Modal Account Setup
1. Sign up at [modal.com](https://modal.com/).
2. Install the `modal` package in your Python virtual environment with `pip install modal`.
3. Configure a Modal token in your environment via `python3 -m modal setup`.
4. To monitor training with Weights and Biases, create a [secret](https://modal.com/secrets) named `my-wandb-secret` in Modal, requiring only the `WANDB_API_KEY` from your Weights and Biases account's [Authorize page](https://wandb.ai/authorize).

## Training
Initiate training with:
```shell
modal run train.py

```

Options:
- `--detach`: keeps the app running if your local process ends or disconnects.
```modal run --detach train.py```
- `--run_id`: assign a custom ID to track training sessions.
```modal run train.py --run_id <run_id>```
- `--resume-from-checkpoint`: continue training from a specific saved checkpoint.
```modal run train.py --resume-from-checkpoint /results/<checkpoint-number>```

Verify that adapter weights are saved in your results volume:
```modal volume ls results-vol```

## Inference
Test your model post-fine-tuning with:
```modal run inference.py --run_id <run_id>```


## Next Steps
- Deploy your model's inference function via a Modal [web endpoint](https://modal.com/docs/guide/webhooks). Modal's serverless scaling means no cost for maintaining an endpoint. For implementation examples, see the [QuiLLMan](https://github.com/modal-labs/quillman/) repository, which features a FastAPI server setup (`quillman/src/app.py`).
- Consider fine-tuning additional models. For models exceeding single-GPU capacity, our [Llama finetuning repository](https://github.com/modal-labs/llama-finetuning/) offers FSDP for optimized multi-GPU scaling.


## Fine-tuning Tips and Observations

- **Learning Rate Adjustment**: When operating with smaller batch sizes, consider reducing the learning rate to maintain training stability.
- **Grad Clip and Weight Decay**: In my experience, adjustments to gradient clipping and weight decay weren't necessary, but your mileage may vary (YMMV). It's worth experimenting to see what works best for your specific setup.
- **Data Volume**: Ensuring a sufficient amount of data is critical. I recommend using more than 1,000 samples for effective training.
- **Epochs and Sample Size**: My training involved 3 epochs over 40,000 samples. The model showed signs of improvement, indicating the need for further experimentation with the number of epochs to optimize performance.
- **Evaluating Model Performance**: To accurately gauge whether your model is improving, overfitting, or deteriorating, incorporate evaluation phases using data not included in the training set. For tasks like code completion, consider evaluating on the MBPP validation set or any other custom dataset you've prepared.
- **Fully Sharded Data Parallelism (FSDP) Options**: If your setup allows, use `backward_prefetch=BackwardPrefetch.BACKWARD_PRE` to leverage GPU memory more efficiently. Alternatively, `backward_prefetch=BackwardPrefetch.BACKWARD_POST` might be an option. Note that setting this to `None` was necessary to avoid out-of-memory (OOM) errors.
