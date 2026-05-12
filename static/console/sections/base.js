orbitConsole.fetchJson('/api/console/base/contacts').then(d=>{document.getElementById('app').innerHTML='<pre>'+JSON.stringify(d,null,2)+'</pre>';});
