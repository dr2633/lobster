# Integrating ESM3-Open-Small in the Lobster Project

This guide outlines the steps to integrate ESM3-open-small from Evolutionary Scale into the Lobster project. ESM3 is a highly scalable protein language model that enhances protein sequence generation and structure prediction.

## Step 1: Environment Setup

1. **Install Dependencies**:
    Make sure to install the necessary packages including `esm` and `huggingface_hub`.
    ```bash
    pip install esm huggingface_hub
    ```

2. **Authentication**:
    Create an account on HuggingFace, accept the non-commercial license for ESM3, and obtain an API key with "Read" permissions.

    - To authenticate in your Python environment, run the following:
    ```python
    from huggingface_hub import login
    login()  # Enter your HuggingFace API key when prompted
    ```

## Step 2: Model Integration

1. **Loading the Model**:
    After authentication, load the `esm3-open-small` model from the HuggingFace model hub. Ensure you are using the proper device (`cuda` for GPU or `cpu` for CPU environments).
    ```python
    from esm.models.esm3 import ESM3
    from esm.sdk.api import ESM3InferenceClient

    # Load the ESM3-open-small model
    model: ESM3InferenceClient = ESM3.from_pretrained("esm3_sm_open_v1").to("cuda")  # or "cpu"
    ```

2. **Protein Generation Example**:
    You can now generate a protein sequence using the model as shown below:
    ```python
    from esm.sdk.api import ESMProtein, GenerationConfig

    # Generate a protein sequence
    def generate_protein_sequence(prompt):
        protein = ESMProtein(sequence=prompt)
        protein = model.generate(protein, GenerationConfig(track="sequence", num_steps=8, temperature=0.7))
        return protein
    ```

## Step 3: Implementing in Lobster

1. **Custom Functions**:
    Create custom functions or workflows that leverage ESM3 to generate protein sequences or predict protein structures. Integrate these workflows into Lobster.

    For example, you could add a function to generate sequences from a prompt and use the Lobster data pipeline to feed sequences into ESM3:
    ```python
    def generate_protein_structure(protein_sequence):
        protein = ESMProtein(sequence=protein_sequence)
        protein = model.generate(protein, GenerationConfig(track="structure", num_steps=8))
        return protein
    ```

2. **Test and Validate**:
    Ensure your integration is thoroughly tested:
    - Write unit tests to verify the functions are working as expected.
    - Validate the model's output against known datasets or benchmarks.

## Step 4: Documentation and Compliance

1. **Update Documentation**:
    Update the Lobster project’s documentation to reflect the new ESM3 functionality. Ensure users know how to install the required packages, authenticate, and use the model.

    Example of how to run a protein generation:
    ```bash
    python generate_protein_sequence.py
    ```

2. **Compliance with License**:
    The `esm3-open-small` model is released under a non-commercial license. Ensure that all users of the Lobster project are aware of the license restrictions, including:
    - The model can only be used for non-commercial purposes.
    - Attribution to Evolutionary Scale is required when using the model.
    - Derivative works must also comply with the non-commercial terms.

## Step 5: Community Engagement and Feedback

1. **Feedback**:
    Engage with the Lobster community via discussions or issue tracking to get feedback on the integration and improve upon it.

2. **Continual Updates**:
    Monitor updates from the Evolutionary Scale team for new versions of ESM3 or related tools. Plan updates for Lobster based on this.

## License

The ESM3 model is available under a non-commercial license. Please review the full license in the [LICENSE.md](https://huggingface.co/EvolutionaryScale/esm3/blob/main/LICENSE.md) document.

## Conclusion

By integrating ESM3 into Lobster, we have expanded the project's capabilities for protein sequence analysis and structure prediction. Ensure compliance with the licensing terms and keep improving the integration based on feedback.
"""

# Saving the markdown content to a file
markdown_filename = "/mnt/data/esm3_integration_lobster.md"
with open(markdown_filename, "w") as file:
    file.write(esm3_markdown_content)

markdown_filename
