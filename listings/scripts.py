class Scripts:

  def create_pois():
    all_names = ['Whittington Hospital', "St Mark's Hospital", "St Charles' Hospital", 'University Hospital Lewisham', 'Wilson Hospital', 'The Gordon Hospital', 'Royal London Hospital', 'Royal Brompton Hospital', "Queen's Hospital", 'Princess Royal University Hospital', 'Mile End Hospital', 'Lambeth Hospital', 'Harold Wood Hospital', 'Harefield Hospital', 'Hammersmith Hospital', 'Ealing Hospital', 'Dulwich Community Hospital', 'Chelsea and Westminster Hospital', 'Chase Farm Hospital', 'Charing Cross Hospital', 'MiddleSex Hospital', 'Cassel Hospital', 'Barnet Hospital', "St George's Hospital", 'Kingston University', 'Royal Veterinary College University of London', 'SOAS, University of London', "St George's, University of London", "St Mary's University, Twickenham", 'The London Institute of Banking and Finance', 'The Royal Central School of Speech and Drama', 'Trinity Laban', 'University College London', 'University of East London', 'University of Greenwich', 'University of Roehampton', 'University of West London', 'Vicarage Road Stadium', 'White Hart Lane', 'The Matchroom Stadium', 'Emirates Stadium', 'Loftus Road Stadium', 'London Stadium', 'The Valley', 'The Den', 'Stamford Bridge', 'Craven Cottage', 'Griffin Park', 'Kingsmeadow', 'Selhurst Park Stadium', 'Wembley Stadium']
    all_types = ['Hospital', 'Hospital', 'Hospital', 'Hospital', 'Hospital', 'Hospital', 'Hospital', 'Hospital', 'Hospital', 'Hospital', 'Hospital', 'Hospital', 'Hospital', 'Hospital', 'Hospital', 'Hospital', 'Hospital', 'Hospital', 'Hospital', 'Hospital', 'Hospital', 'Hospital', 'Hospital', 'Hospital', 'University', 'University', 'University', 'University', 'University', 'University', 'University', 'University', 'University', 'University', 'University', 'University', 'University', 'Stadium', 'Stadium', 'Stadium', 'Stadium', 'Stadium', 'Stadium', 'Stadium', 'Stadium', 'Stadium', 'Stadium', 'Stadium', 'Stadium', 'Stadium', 'Stadium']
    all_lat = [51.566539919589, 51.5757754408871, 51.5222402820392, 51.4537711952925, 51.3974223408796, 51.4922145396458, 51.5174967021095, 51.489000981662, 51.5688917047996, 51.3660839826897, 51.5250533540902, 51.466191063443, 51.5923929621923, 51.6068775742203, 51.5169910722404, 51.5075543906472, 51.4587934645253, 51.4843813173448, 51.6666528216533, 51.4868087102219, 51.5310440943572, 51.4328448059403, 51.6503419109224, 51.4266647582904, 51.4101811532835, 51.5367587450011, 51.5223967086879, 51.4270586124102, 51.4362384977038, 51.5099321570412, 51.544230673054, 51.4833010261379, 51.524699359837, 51.5075966686703, 51.4818654845662, 51.4581115096442, 51.50687192394, 51.6497380998579, 51.6040064853733, 51.5599873431841, 51.5551260784442, 51.5091207906676, 51.5384258684747, 51.4869750939208, 51.4857202302047, 51.4814140059209, 51.4746907618323, 51.4879254090706, 51.4051060328007, 51.3979290062806, 51.5558025659932]
    all_lng = [-0.140065121477782, -0.321541201314411, -0.217923586260206, -0.0172582871048198, -0.16271707730855, -0.136127934975052, -0.0594398450459132, -0.170717582121646, 0.180489919004021, 0.0580437091961461, -0.0420372140894369, -0.12247995642135, 0.224226816689896, -0.482565617780888, -0.2357569274136, -0.345861291358561, -0.0814062791533554, -0.181937836822963, -0.102726671753801, -0.21972596381064, -0.269807363247629, -0.30843812148379, -0.213788821803319, -0.174356442616226, -0.293743665227551, -0.133841969912085, -0.129495036821241, -0.174621392087661, -0.334593090800721, -0.0844096828461803, -0.174391404289801, -0.00692335592494486, -0.13435123866868, 0.0650861552268519, -0.00282114824616996, -0.244403029433868, -0.303254216054838, -0.401769722694477, -0.0658280118174663, -0.0124776674356585, -0.107925563740711, -0.232078255791181, -0.0162818367535218, 0.0367547402907043, -0.0510580055948859, -0.190717127528249, -0.221543867438802, -0.302838301611634, -0.282310080118838, -0.0859447915549685, -0.279908938784692]
    return all_names, all_types, all_lat, all_lng
