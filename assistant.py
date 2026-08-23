#!/usr/bin/env python3
"""
assistant.py — terminal assistant inference script.

Loads the LoRA-fine-tuned Qwen3.5-0.8B model (trained in Terminal_Assistant.ipynb)
and turns a natural-language prompt into a shell command.

Usage:
    python3 assistant.py "list all files including hidden ones"
"""

import sys

# Path to the merged model saved by the notebook
# (model.save_pretrained_merged("/content/qwen35_merged", ...))
MODEL_PATH = "/src/merged_model_folder"


def main():
    if len(sys.argv) < 2:
        print("Usage: assistant.py <prompt>", file=sys.stderr)
        sys.exit(1)

    prompt = sys.argv[1]

    # Imported here so --help / usage errors above don't pay the import cost
    import torch
    from transformers import AutoModelForCausalLM, AutoTokenizer

    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_PATH,
        torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
        device_map="auto" if torch.cuda.is_available() else None,
    )

    # Same ChatML format used during training
    text = (
        f"<|im_start|>user\n"
        f"{prompt}"
        f"<|im_end|>\n"
        f"<|im_start|>assistant\n"
    )

    inputs = tokenizer(text, return_tensors="pt")
    if torch.cuda.is_available():
        inputs = {k: v.to(model.device) for k, v in inputs.items()}

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=128,
            do_sample=False,   # deterministic — we want a command, not a story
            temperature=1.0,
            pad_token_id=tokenizer.eos_token_id,
        )

    generated = outputs[0][inputs["input_ids"].shape[1]:]
    response = tokenizer.decode(generated, skip_special_tokens=True).strip()

    print(response)


if __name__ == "__main__":
    main()