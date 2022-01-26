--
-- PostgreSQL database dump
--

-- Dumped from database version 14.1 (Ubuntu 14.1-2.pgdg20.04+1)
-- Dumped by pg_dump version 14.1 (Ubuntu 14.1-2.pgdg20.04+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: tourism; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE tourism WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'en_US.UTF-8';


ALTER DATABASE tourism OWNER TO postgres;

\connect tourism

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: place_table; Type: TABLE; Schema: places; Owner: postgres
--

CREATE TABLE places.place_table (
    id integer NOT NULL,
    name text,
    description text,
    thumbnail_url text
);


ALTER TABLE places.place_table OWNER TO postgres;

--
-- Name: TABLE place_table; Type: COMMENT; Schema: places; Owner: postgres
--

COMMENT ON TABLE places.place_table IS 'This table describes all the amsterdam places off interests';


--
-- Name: place_table_id_seq; Type: SEQUENCE; Schema: places; Owner: postgres
--

CREATE SEQUENCE places.place_table_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE places.place_table_id_seq OWNER TO postgres;

--
-- Name: place_table_id_seq; Type: SEQUENCE OWNED BY; Schema: places; Owner: postgres
--

ALTER SEQUENCE places.place_table_id_seq OWNED BY places.place_table.id;


--
-- Name: place_table id; Type: DEFAULT; Schema: places; Owner: postgres
--

ALTER TABLE ONLY places.place_table ALTER COLUMN id SET DEFAULT nextval('places.place_table_id_seq'::regclass);


--
-- Data for Name: place_table; Type: TABLE DATA; Schema: places; Owner: postgres
--

COPY places.place_table (id, name, description, thumbnail_url) FROM stdin;
1	Rijks Museum	The Rijksmuseum is a Dutch national museum dedicated to arts and history in Amsterdam. The museum is located at the Museum Square in the borough Amsterdam South, close to the Van Gogh Museum, the Stedelijk Museum Amsterdam, and the Concertgebouw.	\N
2	Van Gogh Museum	The Van Gogh Museum is a Dutch art museum dedicated to the works of Vincent van Gogh and his contemporaries in the Museum Square in Amsterdam South, close to the Stedelijk Museum, the Rijksmuseum, and the Concertgebouw.	\N
3	Jordaan Neighborhood	Jordaan is the most popular of Amsterdam's neighborhoods and is well-known for its mix of residential areas with garden courtyards, lively markets, and upscale boutiques and eateries. The area is also home to plenty of fun things to do, from taking a pleasant stroll along the many picturesque streets to spending time visiting the many top-rated tourist attractions located here.\n\nAlthough best known as the location of Anne Frank House, the area is also home to lesser-known treasures like the Woonboots Museum, a floating museum dedicated to houseboats, and the interesting (honestly!) Amsterdam Cheese Museum.	\N
4	Vondelpark	The largest and most visited park in Amsterdam, Vondelpark occupies 120 acres and contains no end of fun things to do. In addition to expanses of green space dotted by peaceful ponds and traversed by ample paths, the park is home to a lovely rose garden featuring more than 70 different types of the flower.\n\nIt also has a variety of sculptures and statues, playgrounds, and other recreational facilities, including rollerblade rental and the Vondelpark Open Air Theater, which serves as a venue for musical and stage productions from May through September.	\N
5	Dam Square	Dam Square is one of the most tourist-packed areas of Amsterdam, and for good reason. Its most prominent feature is the 17th-century Royal Palace (Koninklijk Palace), former home of the Dutch royal family and present-day venue for royal functions.\n\nDam Square is also home to top tourist attractions such as the New Church (Nieuwe Kerk); Madame Tussauds wax museum; and the National Memorial Statue, which is dedicated to Dutch soldiers who lost their lives in World War II.	\N
6	Royal Palace of Amsterdam	Formerly the Town Hall, the Royal Palace of Amsterdam (Koninklijk Paleis van Amsterdam) serves as the King's residence when he's in the city. Its construction was a monumental task when started in 1648 and required the sinking of 13,659 piles to support the mammoth structure.\n\nBased upon the architecture of ancient Rome, the exterior is strictly classical, while the interior is magnificently furnished, its apartments decorated with a wealth of reliefs, ornamentation, marble sculptures, and friezes. Check out the spectacular ceiling paintings by Ferdinand Bol and Govert Flinck, pupils of Rembrandt.	\N
7	West Church (Westerkerk)	Located next door to the Anne Frank Museum, Amsterdam's West Church (Westerkerk) is one of the most popular churches to visit in the city. It's certainly one of the most picturesque.\n\nCompleted in 1630, this attractive Renaissance church is unusual due to its many internal and external Gothic features. Its 85-meter tower, popularly known as "Langer Jan" (tall John), is the highest in the city. On the tip of its spire is a large replica of the emperor's crown, placed there in memory of Emperor Maximilian of Austria. Inside the tower, a carillon proclaims the hours.	\N
8	Rembrandt House Museum	Rembrandt, along with his wife Saskia, spent the happiest (and most successful) years of his life in the house on the Jodenbreestraat, now home to the Rembrandt House Museum (Museum Het Rembrandthuis). It was here, in the Jewish Quarter, that he found models for his Biblical themes, and where he painted the sights from his many outings along the canals.\n\nRembrandt lived here for 20 years, and the house has been furnished in 17th-century style with numerous etchings and personal objects. English language guided tours are available.	\N
9	Amsterdam Tower	With its 22 floors, the A'DAM Toren in Amsterdam-Noord towers far above everything and everyone. In the tower you will find various bars, restaurants and a viewpoint with a spectacular view over Amsterdam. 	\N
\.


--
-- Name: place_table_id_seq; Type: SEQUENCE SET; Schema: places; Owner: postgres
--

SELECT pg_catalog.setval('places.place_table_id_seq', 9, true);


--
-- Name: place_table place_table_pk; Type: CONSTRAINT; Schema: places; Owner: postgres
--

ALTER TABLE ONLY places.place_table
    ADD CONSTRAINT place_table_pk PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

