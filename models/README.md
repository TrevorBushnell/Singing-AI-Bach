# Models

These are the models that I use throughout my thesis project. I've included all the setup instructions here:


### DeepBach

To start, you will need to set up the conda environment and the Musescore plugin, with the directions being found in the README file located within the repository.

If you are getting errors when creating the conda environment, change the following lines in `environment.yml`:
* `pytorch=1.0.0` $\to$ `pytorch`
* `torchvision=0.2.1=py_2` $\to$ `torchvision`

After these changes, everything should generate fine.

If you want to generate compositions interactively in Musescore, you will need to run the following command:

```
python [PATH_TO_DEEPBACH]/musescore_flask_server.py
```

However, I don't always want to have to navigate to this repo every time I want to start the server, so I add this line to my `.bash_aliases` file:

```
alias deepbach_musescore='conda deactivate && conda activate deepbach_pytorch && python [PATH_TO_DEEPBACH]/musescore_flask_server.py'
```

Then I can just run `deepbach_musescore` to start the musescore plugin whenever I wish to compose interactively!


### BachBot

**EXPLANATION OF HOW TO SET THIS UP TO COME**


### Coconet

The original codebase can be found [here](https://github.com/magenta/magenta). However, I instead use a Python package where I install magenta using Anaconda as follows:

```
curl https://raw.githubusercontent.com/tensorflow/magenta/main/magenta/tools/magenta-install.sh > /home/tbushnell/Downloads/magenta-install.sh
bash /home/tbushnell/Downloads/magenta-install.sh
rm /home/tbushnell/Downloads/magenta-install.sh0
```

However, if you want to use magenta in your code, you will need to activate the Anaconda environment that is created by running `conda activate magenta` in your terminal (or selecting the apporpriate environment in VSCode).

Then, you can use this starter code to generate chorales:

```python
from magenta.models.coconet import coconet_model

# Load the Coconet model
model = coconet_model.Coconet(
    n_chans=256,  # Number of channels
    n_blocks=6,   # Number of blocks in the model
    n_layers=6    # Number of layers in each block
)

# Provide your prepared input as a sequence
input_sequence = ...

# Generate a harmonized sequence
generated_sequence = model.generate_chorale(input_sequence)

from magenta.music import midi_io

# Save the generated sequence as MIDI
midi_filename = "generated_chorale.mid"
midi_io.note_sequence_to_midi_file(generated_sequence, midi_filename)
```
