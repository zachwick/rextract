# Usage

0. Install and setup [remarking](https://remarking.readthedocs.io/en/latest/usage.html)

1. Get an [access token for your Readwise account](https://readwise.io/access_token), and put it in `upload.py`

2. Use `remarking` to extract all Remarkable highlights to a local `hl.json` via

    remarking run json [folder name] > hl.json

3. Run `upload.py` to upload all extracted highlights to Readwise
    
# License

rextract is licensed under the GNU GPLv3 or later. See [LICENSE.txt](https://github.com/zachwick/rextract/blob/master/LICENSE.txt) for more details.
