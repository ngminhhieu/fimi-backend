use fimi;

//create collections
db.createCollection("sensor");
db.createCollection("forecasting");
// db.createCollection("location_aqi");

//gen fake datas
// db.location_aqi.insert(
//     [
//         {
//             area: 'Hanoi',
//             updated: new Date(),
//             latitude: _rand() * 100,
//             longitude: _rand() * 100,
//             PM2_5: _rand() * 100,
//             temperature: _rand() * 100,
//             humidity: _rand() * 100,
//             status: "Good",
//             activities: "Good for outdoor activities, playing sports, ...",
//             rank: _rand() * 100,
//             history: [_rand() * 100] * 10
//         },
//         {
//             area: 'Danang',
//             updated: new Date(),
//             latitude: _rand() * 100,
//             longitude: _rand() * 100,
//             PM2_5: _rand() * 100,
//             temperature: _rand() * 100,
//             humidity: _rand() * 100,
//             status: "Good",
//             activities: "Good for outdoor activities, playing sports, ...",
//             rank: _rand() * 100,
//             history: [_rand() * 100] * 10
//         },
//         {
//             area: 'Saigon',
//             updated: new Date(),
//             latitude: _rand() * 100,
//             longitude: _rand() * 100,
//             PM2_5: _rand() * 100,
//             temperature: _rand() * 100,
//             humidity: _rand() * 100,
//             status: "Medium",
//             activities: "Breathable, ...",
//             rank: _rand() * 100,
//             history: [_rand() * 100] * 10
//         }
//     ]);
db.forecasting.insert(
    [
        {
            device_id: 1,
            area: "Hanoi",
            updated: new Date(),
            latitude: _rand() * 100,
            longitude: _rand() * 100,
            PM2_5: _rand() * 100,
            PM10: _rand() * 100,
            PM1_0: _rand() * 100,
            temperature: _rand() * 100,
            humidity: _rand() * 100,
            CO: _rand() * 100,
            CO2: _rand() * 100,
            NO2: _rand() * 100,
            O3: _rand() * 100,
            SO2: _rand() * 100
        },
        {
            device_id: 2,
            area: 'Danang',
            updated: new Date(),
            latitude: _rand() * 100,
            longitude: _rand() * 100,
            PM2_5: _rand() * 100,
            PM10: _rand() * 100,
            PM1_0: _rand() * 100,
            temperature: _rand() * 100,
            humidity: _rand() * 100,
            CO: _rand() * 100,
            CO2: _rand() * 100,
            NO2: _rand() * 100,
            O3: _rand() * 100,
            SO2: _rand() * 100
        },
        {
            device_id: 3,
            area: 'Saigon',
            latitude: _rand() * 100,
            longitude: _rand() * 100,
            updated: new Date(),
            PM2_5: _rand() * 100,
            PM10: _rand() * 100,
            PM1_0: _rand() * 100,
            temperature: _rand() * 100,
            humidity: _rand() * 100,
            CO: _rand() * 100,
            CO2: _rand() * 100,
            NO2: _rand() * 100,
            O3: _rand() * 100,
            SO2: _rand() * 100
        }
    ]);
db.sensor.insert(
    [
        {
            device_id: 1,
            area: 'Hanoi',
            latitude: _rand() * 100,
            longitude: _rand() * 100,
            updated: new Date(),
            PM2_5: _rand() * 100,
            PM10: _rand() * 100,
            PM1_0: _rand() * 100,
            temperature: _rand() * 100,
            humidity: _rand() * 100,
            CO: _rand() * 100,
            CO2: _rand() * 100,
            NO2: _rand() * 100,
            O3: _rand() * 100,
            SO2: _rand() * 100,
            history: []
        },
        {
            device_id: 2,
            area: 'Saigon',
            latitude: _rand() * 100,
            longitude: _rand() * 100,
            updated: new Date(),
            PM2_5: _rand() * 100,
            PM10: _rand() * 100,
            PM1_0: _rand() * 100,
            temperature: _rand() * 100,
            humidity: _rand() * 100,
            CO: _rand() * 100,
            CO2: _rand() * 100,
            NO2: _rand() * 100,
            O3: _rand() * 100,
            SO2: _rand() * 100,
            history: []
        },
        {
            device_id: 3,
            area: 'Danang',
            latitude: _rand() * 100,
            longitude: _rand() * 100,
            updated: new Date(),
            PM2_5: _rand() * 100,
            PM10: _rand() * 100,
            PM1_0: _rand() * 100,
            temperature: _rand() * 100,
            humidity: _rand() * 100,
            CO: _rand() * 100,
            CO2: _rand() * 100,
            NO2: _rand() * 100,
            O3: _rand() * 100,
            SO2: _rand() * 100,
            history: []
        }
    ]);