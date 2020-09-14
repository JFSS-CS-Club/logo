# JFSS CS Club Logo

This logo is designed using LaTeX, and converted using ImageMagick

## Building

1. Build the PDF file: `pdflatex src/logo.tex logo.pdf`
1. Convert to a PNG: `convert -density 1000 logo.pdf -quality 90 -trim -background white -alpha remove -alpha off -bordercolor white -border 20 -resize '1024x1024>' -gravity center -extent 1024x1024 dist/logo.png`
