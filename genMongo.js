use fimi;

//create collections
db.createCollection("sensor");
db.createCollection("forecasting");
db.createCollection("location_aqi");

//gen fake datas
db.location_aqi.insert(
    [
        {
            area: 'Hanoi',
            updated: Date(),
            latitude: _rand() * 100,
            longitude: _rand() * 100,
            PM2_5: _rand() * 100,
            temperature: _rand() * 100,
            humidity: _rand() * 100,
            status: "Good",
            activities: "Good for outdoor activities, playing sports, ...",
            rank: _rand() * 100,
            history: [_rand() * 100] * 10
        },
        {
            area: 'Danang',
            updated: Date(),
            latitude: _rand() * 100,
            longitude: _rand() * 100,
            PM2_5: _rand() * 100,
            temperature: _rand() * 100,
            humidity: _rand() * 100,
            status: "Good",
            activities: "Good for outdoor activities, playing sports, ...",
            rank: _rand() * 100,
            history: [_rand() * 100] * 10
        },
        {
            area: 'Saigon',
            updated: Date(),
            latitude: _rand() * 100,
            longitude: _rand() * 100,
            PM2_5: _rand() * 100,
            temperature: _rand() * 100,
            humidity: _rand() * 100,
            status: "Medium",
            activities: "Breathable, ...",
            rank: _rand() * 100,
            history: [_rand() * 100] * 10
        }
    ]);
db.forecasting.insert(
    [
        {
            area: "Hanoi",
            datetime: Date(),
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
            area: 'Danang',
            datetime: Date(),
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
            area: 'Saigon',
            datetime: Date(),
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
            datetime: Date(),
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
            datetime: Date(),
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
            datetime: Date(),
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