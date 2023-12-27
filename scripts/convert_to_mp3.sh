# THIS SCRIPT GENERATES MIDIS, PDFS, AND MUSICXML FILES FOR ALL GENERATED MUSIC

FILE_EXT_1=".mp3"
FILE_EXT_2=".mid"
FILE_EXT_3=".mxl"
FILE_EXT_4=".pdf"


for SUBDIR in ./../ai-music/*/; do
	# iterate over all musescore files
	for file in "$SUBDIR"*.mscz; do
		newfpath1="${file:0:-5}$FILE_EXT_1"
		newfpath2="${file:0:-5}$FILE_EXT_2"
		newfpath3="${file:0:-5}$FILE_EXT_4"
		mscore3 -o $newfpath1 $file
		mscore3 -o $newfpath2 $file
		mscore3 -o $newfpath3 $file
	done

	# iterate over all the midi files
	for file in "$SUBDIRECTORY"*.mid; do
		newfpath1="${file:0:-4}$FILE_EXT_1"
		newfpath2="${file:0:-4}$FILE_EXT_3"
		newfpath3="${file:0:-4}$FILE_EXT_4"
		mscore3 -o $newfpath1 $file
		mscore3 -o $newfpath2 $file
		mscore3 -o $newfpath3 $file
	done
done