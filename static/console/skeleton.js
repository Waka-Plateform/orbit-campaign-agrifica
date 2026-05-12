window.orbitConsole={fetchJson:async(url,opts={})=>{const r=await fetch(url,opts);if(!r.ok)throw new Error(await r.text());return r.json();}};
