# swc2022-group26
Software Cointainerization Project

## Flask Project
- Install all dependencies in a venv from requirements.txt
- run `start.py` which will start the Flask application with a static webpage showing results from `/web/default.py`
- The REST APIs are configured in `routes.py` that routes to `/apis/model.py` where you will have the *GET* and *POST* method.
- The APIS for now are `http://localhost:8000/api/swc` in GET and POST method. Try running it in postman. :)
- Thats all folks :)

## Frontend
- Change your terminal directory to `swc/frontend`
- Run the local network using command:
```
npm run serve
```
- Visit locahost under the address: ` http://localhost:8080/` 

## Database
- For now install postgresql in the localhost with username as `postgres` and password.
- Run requirements.txt again to install postgres adapter dependecies and extra others: `Flask-SQLAlchemy==2.5.1
psycopg2-binary==2.9.3
dataclasses-json==0.5.6`
- change the postgres configuration in `swc/src/swc/conf/conf.json`
- "SQLALCHEMY_DATABASE_URI": "postgresql+psycopg2://{$POSTGRES_USERNAME}:{$POSTGRES_PASSWORD}@localhost/tourism".
- Give valid $POSTGRES_USERNAME} and {$POSTGRES_PASSWORD}.
- Run `swc/db/insert_dummy_values.sql` in postgres before running application to add dummy values and create the table and schema.
- Run Flask again
- Now the existing apis: /api will have both POST and GET method.
- Try it out:
  ```commandline
  curl --location --request POST 'http://localhost:8000/api' --data-raw '' 
  ```
  ```commandline
  curl --location --request POST 'http://localhost:8000/api' --header 'Content-Type: application/json' --data-raw '{"id": 2}'
    ```
  ```commandline
  curl --location --request GET 'http://localhost:8000/api' --data-raw ''
  ```
  ```commandline
  curl --location --request GET 'http://localhost:8000/api?id=3' --data-raw ''
  ```
- Example Responses:
  - ```json
    {
      "uuid": "a9c9a4ec-0554-42c5-9c66-91b772047b96",
      "places": [
        {
          "id": 1,
          "name": "Rijks Museum",
          "description": "The Rijksmuseum is a Dutch national museum dedicated to arts and history in Amsterdam. The museum is located at the Museum Square in the borough Amsterdam South, close to the Van Gogh Museum, the Stedelijk Museum Amsterdam, and the Concertgebouw."
        }
      ]
    }
    ```
  - ```json
    {
    "uuid": "fe9ffb13-dfd2-4d36-b251-c4ce2ce00e67",
    "places": [
        {
            "id": 1,
            "name": "Rijks Museum",
            "description": "The Rijksmuseum is a Dutch national museum dedicated to arts and history in Amsterdam. The museum is located at the Museum Square in the borough Amsterdam South, close to the Van Gogh Museum, the Stedelijk Museum Amsterdam, and the Concertgebouw."
        },
        {
            "id": 2,
            "name": "Van Gogh Museum",
            "description": "The Van Gogh Museum is a Dutch art museum dedicated to the works of Vincent van Gogh and his contemporaries in the Museum Square in Amsterdam South, close to the Stedelijk Museum, the Rijksmuseum, and the Concertgebouw."
        },
        {
            "id": 3,
            "name": "Jordaan Neighborhood",
            "description": "Jordaan is the most popular of Amsterdam's neighborhoods and is well-known for its mix of residential areas with garden courtyards, lively markets, and upscale boutiques and eateries. The area is also home to plenty of fun things to do, from taking a pleasant stroll along the many picturesque streets to spending time visiting the many top-rated tourist attractions located here.\n\nAlthough best known as the location of Anne Frank House, the area is also home to lesser-known treasures like the Woonboots Museum, a floating museum dedicated to houseboats, and the interesting (honestly!) Amsterdam Cheese Museum."
        },
        {
            "id": 4,
            "name": "Vondelpark",
            "description": "The largest and most visited park in Amsterdam, Vondelpark occupies 120 acres and contains no end of fun things to do. In addition to expanses of green space dotted by peaceful ponds and traversed by ample paths, the park is home to a lovely rose garden featuring more than 70 different types of the flower.\n\nIt also has a variety of sculptures and statues, playgrounds, and other recreational facilities, including rollerblade rental and the Vondelpark Open Air Theater, which serves as a venue for musical and stage productions from May through September."
        },
        {
            "id": 5,
            "name": "Dam Square",
            "description": "Dam Square is one of the most tourist-packed areas of Amsterdam, and for good reason. Its most prominent feature is the 17th-century Royal Palace (Koninklijk Palace), former home of the Dutch royal family and present-day venue for royal functions.\n\nDam Square is also home to top tourist attractions such as the New Church (Nieuwe Kerk); Madame Tussauds wax museum; and the National Memorial Statue, which is dedicated to Dutch soldiers who lost their lives in World War II."
        },
        {
            "id": 6,
            "name": "Royal Palace of Amsterdam",
            "description": "Formerly the Town Hall, the Royal Palace of Amsterdam (Koninklijk Paleis van Amsterdam) serves as the King's residence when he's in the city. Its construction was a monumental task when started in 1648 and required the sinking of 13,659 piles to support the mammoth structure.\n\nBased upon the architecture of ancient Rome, the exterior is strictly classical, while the interior is magnificently furnished, its apartments decorated with a wealth of reliefs, ornamentation, marble sculptures, and friezes. Check out the spectacular ceiling paintings by Ferdinand Bol and Govert Flinck, pupils of Rembrandt."
        },
        {
            "id": 7,
            "name": "West Church (Westerkerk)",
            "description": "Located next door to the Anne Frank Museum, Amsterdam's West Church (Westerkerk) is one of the most popular churches to visit in the city. It's certainly one of the most picturesque.\n\nCompleted in 1630, this attractive Renaissance church is unusual due to its many internal and external Gothic features. Its 85-meter tower, popularly known as \"Langer Jan\" (tall John), is the highest in the city. On the tip of its spire is a large replica of the emperor's crown, placed there in memory of Emperor Maximilian of Austria. Inside the tower, a carillon proclaims the hours."
        },
        {
            "id": 8,
            "name": "Rembrandt House Museum",
            "description": "Rembrandt, along with his wife Saskia, spent the happiest (and most successful) years of his life in the house on the Jodenbreestraat, now home to the Rembrandt House Museum (Museum Het Rembrandthuis). It was here, in the Jewish Quarter, that he found models for his Biblical themes, and where he painted the sights from his many outings along the canals.\n\nRembrandt lived here for 20 years, and the house has been furnished in 17th-century style with numerous etchings and personal objects. English language guided tours are available."
        },
        {
            "id": 9,
            "name": "Amsterdam Tower",
            "description": "With its 22 floors, the A'DAM Toren in Amsterdam-Noord towers far above everything and everyone. In the tower you will find various bars, restaurants and a viewpoint with a spectacular view over Amsterdam. "
        }
      ]
    }
    ``` 
