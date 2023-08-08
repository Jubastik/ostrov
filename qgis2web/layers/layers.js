var wms_layers = [];

var lyr_topo_clip_0 = new ol.layer.Image({
                            opacity: 1,
                            title: "topo_clip",
                            
                            
                            source: new ol.source.ImageStatic({
                               url: "./layers/topo_clip_0.png",
    attributions: ' ',
                                projection: 'EPSG:3857',
                                alwaysInRange: true,
                                imageExtent: [3323366.330239, 8656029.161382, 3347100.208261, 8679752.354192]
                            })
                        });
var format_landscape_1 = new ol.format.GeoJSON();
var features_landscape_1 = format_landscape_1.readFeatures(json_landscape_1, 
            {dataProjection: 'EPSG:4326', featureProjection: 'EPSG:3857'});
var jsonSource_landscape_1 = new ol.source.Vector({
    attributions: ' ',
});
jsonSource_landscape_1.addFeatures(features_landscape_1);
var lyr_landscape_1 = new ol.layer.Vector({
                declutter: true,
                source:jsonSource_landscape_1, 
                style: style_landscape_1,
                interactive: true,
    title: 'landscape<br />\
    <img src="styles/legend/landscape_1_0.png" /> водоёмы<br />\
    <img src="styles/legend/landscape_1_1.png" /> Пляжи<br />\
    <img src="styles/legend/landscape_1_2.png" /> Смешанный лес<br />\
    <img src="styles/legend/landscape_1_3.png" /> Смешанный лес на скалах<br />\
    <img src="styles/legend/landscape_1_4.png" /> Луга<br />\
    <img src="styles/legend/landscape_1_5.png" /> Населенные пункты<br />\
    <img src="styles/legend/landscape_1_6.png" /> Хвойный лес<br />\
    <img src="styles/legend/landscape_1_7.png" /> Лиственный лес<br />\
    <img src="styles/legend/landscape_1_8.png" /> Хвойный лес по болоту<br />\
    <img src="styles/legend/landscape_1_9.png" /> Болота<br />\
    <img src="styles/legend/landscape_1_10.png" /> <br />\
    <img src="styles/legend/landscape_1_11.png" /> Лиственный лес на скалах<br />\
    <img src="styles/legend/landscape_1_12.png" /> Береговые скалы<br />\
    <img src="styles/legend/landscape_1_13.png" /> Хвойное редколесье на скалах<br />'
        });
var format_roads_2 = new ol.format.GeoJSON();
var features_roads_2 = format_roads_2.readFeatures(json_roads_2, 
            {dataProjection: 'EPSG:4326', featureProjection: 'EPSG:3857'});
var jsonSource_roads_2 = new ol.source.Vector({
    attributions: ' ',
});
jsonSource_roads_2.addFeatures(features_roads_2);
var lyr_roads_2 = new ol.layer.Vector({
                declutter: true,
                source:jsonSource_roads_2, 
                style: style_roads_2,
                interactive: true,
                title: '<img src="styles/legend/roads_2.png" /> roads'
            });
var format_rivers_3 = new ol.format.GeoJSON();
var features_rivers_3 = format_rivers_3.readFeatures(json_rivers_3, 
            {dataProjection: 'EPSG:4326', featureProjection: 'EPSG:3857'});
var jsonSource_rivers_3 = new ol.source.Vector({
    attributions: ' ',
});
jsonSource_rivers_3.addFeatures(features_rivers_3);
var lyr_rivers_3 = new ol.layer.Vector({
                declutter: true,
                source:jsonSource_rivers_3, 
                style: style_rivers_3,
                interactive: true,
                title: '<img src="styles/legend/rivers_3.png" /> rivers'
            });

lyr_topo_clip_0.setVisible(true);lyr_landscape_1.setVisible(true);lyr_roads_2.setVisible(true);lyr_rivers_3.setVisible(true);
var layersList = [lyr_topo_clip_0,lyr_landscape_1,lyr_roads_2,lyr_rivers_3];
lyr_landscape_1.set('fieldAliases', {'fid': 'fid', 'type': 'type', });
lyr_roads_2.set('fieldAliases', {'fid': 'fid', });
lyr_rivers_3.set('fieldAliases', {'fid': 'fid', });
lyr_landscape_1.set('fieldImages', {'fid': 'TextEdit', 'type': 'ValueMap', });
lyr_roads_2.set('fieldImages', {'fid': 'TextEdit', });
lyr_rivers_3.set('fieldImages', {'fid': 'TextEdit', });
lyr_landscape_1.set('fieldLabels', {'fid': 'header label', 'type': 'header label', });
lyr_roads_2.set('fieldLabels', {'fid': 'header label', });
lyr_rivers_3.set('fieldLabels', {'fid': 'header label', });
lyr_rivers_3.on('precompose', function(evt) {
    evt.context.globalCompositeOperation = 'normal';
});