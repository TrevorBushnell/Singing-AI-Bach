BUNDLE_PATH='polyphony_rnn.mag'
PRIMER_MELODY=$(cat "./melodies/$1.txt")

polyphony_rnn_generate \
--bundle_file=${BUNDLE_PATH} \
--output_dir=/magenta-data/magenta_output/$1 \
--num_outputs=3 \
--num_steps=512 \
--primer_melody=$PRIMER_MELODY
#--primer-midi='twinkle_twinkle_melody.mid'
#--condition_on_primer=false \
--inject_primer_during_generation=true

mv magenta_output/$1/*_1.mid magenta_output/$1/$1_magenta_1.mid
mv magenta_output/$1/*_2.mid magenta_output/$1/$1_magenta_2.mid
mv magenta_output/$1/*_3.mid magenta_output/$1/$1_magenta_3.mid
