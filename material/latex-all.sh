function triplelatex {
    filename=$(basename "$1")
    filename="${filename%.*}"
    mkdir -p ./.latex
    if [ -d "./.latex/_minted-"$filename ]; then
       mv "./.latex/_minted-"$filename ./
    fi
    pdflatex -shell-escape -output-directory "./.latex" "$1"
    pdflatex -shell-escape -output-directory "./.latex" "$1"
    pdflatex -shell-escape -output-directory "./.latex" "$1"
    mv ./.latex/*.pdf ./
    mv _minted-$filename ./.latex
}

cd assignment1
triplelatex as1.tex
cd ../week1
triplelatex ex1.tex
triplelatex sol1.tex
cd ../week2
triplelatex ex2.tex
triplelatex sol2.tex
cd ../week3
triplelatex ex3.tex
triplelatex sol3.tex
cd ../week4
triplelatex ex4.tex
triplelatex sol4.tex
cd ../week5
triplelatex ex5.tex
triplelatex sol5.tex
