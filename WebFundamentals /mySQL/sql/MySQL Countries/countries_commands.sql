
-- 1 --
select countries.name as country_name, languages.language, languages.percentage from languages 
join countries on languages.country_id = countries.id and languages.language = "Slovene" order by languages.percentage desc;


-- 2 --
select countries.name as country_name, count(cities.country_id) as cities from cities 
join countries where cities.country_id = countries.id
group by country_name order by cities desc;


-- 3 --
select cities.name, cities.population, cities.country_id from cities
where country_id = 136 and cities.population > 500000 order by cities.population desc;


-- 4 --
select countries.name, languages.language, languages.percentage from languages join countries
where languages.country_id = countries.id  and percentage > 89 
order by languages.percentage desc;


-- 5 --
select countries.name, countries.surface_area, countries.population from countries where surface_area < 501 and countries.population > 100000;


-- 6 -- 
select countries.name, countries.government_form, countries.capital, countries.life_expectancy 
from countries
where countries.capital > 200 and countries.life_expectancy > 75 and countries.government_form = 'Constitutional Monarchy';


-- 7 --
select countries.name, cities.name, cities.district, cities.population
from countries join cities 
where countries.name = "Argentina" and cities.district = 'Buenos Aires' and cities.population > 500000;


-- 8 --
select countries.region, count(countries.id) as countries from countries
group by region
order by count(countries.id) desc;