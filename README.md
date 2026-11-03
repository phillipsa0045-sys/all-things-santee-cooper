# All Things Santee Cooper Conditions Dashboard
Grumpywerks public conditions dashboard. The public page is index.html, and editorial.json contains the shared daily fishing outlook and approved public links.

## GitHub Pages setup
Go to repository Settings → Pages → Build and deployment. Set Source to Deploy from a branch, choose main and /(root), and Save. Public address: https://phillipsa0045-sys.github.io/all-things-santee-cooper/

## Publishing your report
Edit editorial.json on GitHub, insert updated_at with a timezone offset, update outlook and canal, and add approved https:// URLs for patreon, youtube, gumroad, facebook, or article. Commit to main. Never put paid GPS coordinates or confidential information into this public repository.

## Verification required before promoting
Check every USGS value against the original gauge, validate vertical datums (Marion and Moultrie may differ), ensure river flow stations represent the intended conditions, and test weather.gov forecast requests in a deployed browser. Missing or stale data must not be represented as verified live observations. Site is not a navigation or boating safety authority.
