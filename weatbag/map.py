HTML_HEAD = """<!DOCTYPE html><html>
<head>
<title>Weatbag map</title>
<style type="text/css">
td {
    text-align: center;
}
table {
    border-collapse:collapse;
}
table,th, td {
    border: 1px solid grey;
}
</style>
</head>
<body><table>
"""

def make_html_map(tiles, destination):
    """Prepare an HTML map (written to destination) from the tiles, which
    should be a mapping of (e, n) -> tile."""
    easts = {e for (e,n) in tiles}
    norths = {n for (e,n) in tiles}
    
    w = destination.write
    w(HTML_HEAD)
    min_e, max_e = min(easts), max(easts)
    for n in range(max(norths), min(norths)-1, -1):
        w("<tr>")
        for e in range(min_e, max_e+1):
            try:
                tile = tiles[(e,n)]
                s = tile.map_word
            except KeyError:
                s = ""
            except AttributeError:
                s = "?"  # Tile exists, but no description given
            w("<td>%s</td>" % s)
        w("</tr>\n")
    
    w("</table>\n</body></html>")

def show_map(tiles):
    "Write a map to a temporary file and load it in a web browser."
    import tempfile, webbrowser
    from urllib.request import pathname2url
    from urllib.parse import urljoin
    file = tempfile.NamedTemporaryFile('w', encoding='utf-8', delete=False)
    make_html_map(tiles, file)
    file.close()
    webbrowser.open(urljoin('file:', pathname2url(file.name)))
