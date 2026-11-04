/* All Things Santee Cooper — private website analytics.
   Activate by entering your own GoatCounter site code below after signup:
   https://www.goatcounter.com/
   Example: const GOATCOUNTER_SITE_CODE = 'my-site-code';
   Do not enter your login, password, or email address.
*/
(function () {
  'use strict';
  const GOATCOUNTER_SITE_CODE = '';
  if (!GOATCOUNTER_SITE_CODE) return;
  if (!/^[a-z0-9][a-z0-9-]*$/i.test(GOATCOUNTER_SITE_CODE)) return;
  const script = document.createElement('script');
  script.async = true;
  script.src = 'https://gc.zgo.at/count.js';
  script.setAttribute('data-goatcounter', 'https://' + GOATCOUNTER_SITE_CODE + '.goatcounter.com/count');
  document.head.appendChild(script);
})();
