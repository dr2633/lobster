import torch
from esm.models.esm3 import ESM3
from esm.sdk.api import ESM3InferenceClient
from esm.sdk.api import ESMProtein, GenerationConfig
from huggingface_hub import login

# Function to authenticate and load ESM3 model
def load_esm3_model():
    # Authenticate using HuggingFace API token
    login()  # Will prompt for your API key if not already done

    # Load the ESM3-open-small model
    model: ESM3InferenceClient = ESM3.from_pretrained("esm3_sm_open_v1").to("cuda")  # or "cpu"
    return model

# Function to generate protein sequence from prompt
def generate_protein_sequence(model, prompt):
    protein = ESMProtein(sequence=prompt)
    protein = model.generate(protein, GenerationConfig(track="sequence", num_steps=8, temperature=0.7))
    return protein

# Function to generate protein structure
def generate_protein_structure(model, protein_sequence):
    protein = ESMProtein(sequence=protein_sequence)
    protein = model.generate(protein, GenerationConfig(track="structure", num_steps=8))
    return protein

# Main execution workflow
if __name__ == "__main__":
    # Example prompt sequence
    prompt_sequence = "DQATSLRILNNGHAFNVEFDDSQDKAVLKGGPLDGTYRLIQFHFHWGSLDGQGSEHTVDKKKYAAELHLVHWNTKYGDFGKAVQQPDGLAVLGIFLKVGSAKPGLQKVVDVLDSIKTKGKSADFTNFDPRGLLPESLDYWTYPGSLTTPP"

    # Load model
    model = load_esm3_model()

    # Generate protein sequence
    generated_protein = generate_protein_sequence(model, prompt_sequence)
    print(f"Generated protein sequence: {generated_protein.sequence}")

    # Generate protein structure
    generated_structure = generate_protein_structure(model, generated_protein.sequence)
    generated_structure.to_pdb("./generated_structure.pdb")
    print("Generated protein structure saved to generated_structure.pdb")
