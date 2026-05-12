orbitConsole.fetchJson('/api/console/channels').then(d=>{document.getElementById('app').innerHTML='<pre>'+JSON.stringify(d,null,2)+'</pre>';});
