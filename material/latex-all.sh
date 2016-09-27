function triplelatex {
    filename=$(basename "$1")
    filename="${filename%.*}"
    mkdir -p ./.latex
    if [ -d "./.latex/_minted-"$filename ]; then
       mv "./.latex/_minted-"$filename ./
    fi
    pdflatex -shell-escape -interaction batchmode -output-directory "./.latex" "$1"
    pdflatex -shell-escape -interaction batchmode -output-directory "./.latex" "$1"
    pdflatex -shell-escape -interaction batchmode -output-directory "./.latex" "$1"
    mv ./.latex/*.pdf ./
    mv _minted-$filename ./.latex
}

for foldername in *; do
    if [[ -d $foldername ]]; then
        cd $foldername
        for filename in *.tex; do
            triplelatex $filename
        done
        cd ..
    fi

done
