


var info = {
    'braiders': { 'title': 'Braiders / Trenzadoras' ,'operators': [ 'trini','luque' ]  },
    'bunching': { 'title': 'Bunching / Cableadoras' ,'operators': [ 'luis'] } , 
    'extruding': {'title': 'Extruders / Extrusoras' ,'operators': [ 'pere']}, 
    'deliveries': {'title': 'Deliveries / Entregas' ,'operators': [ 'carmelo']}  
} 


for(var propt in info){
    cnv = document.getElementById(propt);
    ctx = cnv.getContext("2d");
    ctx.font = "bold 12px sans-serif";
    ctx.fillText(info[propt]['title'],0,10);
    ctx.fillText( info[propt]['operators'] ,0,30);
    
    ctx.fillRect(50, 50, 100, 100)

    alert(propt + ': ' + info[propt]);
}
