Read the book [here](https://chief-puffy-bill.glitch.me)!


This is a tool that assisted in the generation of: Determiner Adjective Noun

Steps to create were:

1. Find a book on Project Gutenberg.  Save the html.  In this case it is `source.html`.
2. Copy the HTML contents of the book (omitting page HTML and Gutenberg notices) into [https://parts-of-speech.info/](https://parts-of-speech.info/)
3. Copy the HTML of that website's output paste into a new html file.  In this case, it was `tagged.html`
4. Run genBook.py to produce `outPutToManicure.html`
5. Manually fix things that this process made errors on and save.  In this case `book.html`.
6. Add page HTML back in to provide styling
7. Sometimes Unicode characters look bad when HTML is served locally.  You may need to host on SSL for things like smart quotes and mdashes to look right.
