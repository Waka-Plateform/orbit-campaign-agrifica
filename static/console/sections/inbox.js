orbitConsole.fetchJson('/api/console/inbox/email').then(d=>{document.getElementById('app').innerHTML='<pre>'+JSON.stringify(d,null,2)+'</pre>';});
