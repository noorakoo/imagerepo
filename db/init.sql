create database imagerepo;
use imagerepo;

CREATE TABLE images (
  title VARCHAR(200),
  link VARCHAR(200),
  descript VARCHAR(200)
);

INSERT INTO images
  (title, link, descript)
  
VALUES
  ('Calypso', 'https://commons.wikimedia.org/wiki/File:%27Calypso%27_Panorama_of_Spirit%27s_View_from_%27Troy%27_(Stereo).jpg', 'Mars: Panorama of Spirits View from Troy'),
  ('Pyramids', 'https://commons.wikimedia.org/wiki/File:%27Pyramids_and_Skull%27_in_Cydonia_region,_perspective_ESA220732.jpg', 'Mars: Pyramids and Skull in Cydonia region, perspective'), 
  ('Crater', 'https://commons.wikimedia.org/wiki/File:(PSP_003201_1335)_Gullies_on_South_Rim_of_Crater_in_Terra_Sirenum_Area.jpg', 'Mars: Gullies on South Rim of Crater in Terra Sirenum Area');