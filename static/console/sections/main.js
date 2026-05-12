orbitConsole.fetchJson('/api/console/main').then(d=>{document.getElementById('app').innerHTML='<pre>'+JSON.stringify(d,null,2)+'</pre>';});
