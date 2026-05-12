orbitConsole.fetchJson('/api/console/dashboard').then(d=>{document.getElementById('app').innerHTML='<pre>'+JSON.stringify(d,null,2)+'</pre>';});
