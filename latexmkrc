$pdflatex = 'lualatex -file-line-error -shell-escape -synctex=1 -halt-on-error -output-directory build.nosync %S %O';
$pdf_mode = 1;
$out_dir = 'build.nosync';
$do_cd = 1;

@default_files = ('2025-05-12_odd_chain_tutorial.tex');

