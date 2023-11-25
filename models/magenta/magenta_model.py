from magenta.models.melody_rnn import melody_rnn_sequence_generator
from magenta.models.shared import sequence_generator_bundle
from magenta.music import sequences_lib

# Load the pre-trained MelodyRNN model bundle
bundle_path = './basic_rnn.mag'
bundle = sequence_generator_bundle.read_bundle_file(bundle_path)
generator_map = sequence_generator_bundle.generator_map_from_bundle(bundle)
generator_id = melody_rnn_sequence_generator.MelodyRnnSequenceGenerator.generator_id
generator = generator_map[generator_id]

# Load the primer melody from a MIDI file
primer_midi_path = './twinkle_twinkle_melody.mid'
primer_sequence = sequences_lib.load_midi_file(primer_midi_path)

# Set the generation parameters
num_steps = 128  # Adjust the number of steps as needed

# Generate the chorale
generated_sequence = generator.generate(primer_sequence, num_steps=num_steps)

# Save the generated sequence as a MIDI file
output_path = 'generated_chorale.mid'
sequences_lib.write_sequence_to_midi_file(generated_sequence, output_path)