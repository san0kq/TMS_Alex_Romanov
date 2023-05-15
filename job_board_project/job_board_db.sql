--
-- PostgreSQL database dump
--

-- Dumped from database version 14.7 (Ubuntu 14.7-0ubuntu0.22.04.1)
-- Dumped by pg_dump version 14.7 (Ubuntu 14.7-0ubuntu0.22.04.1)

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
-- Name: adresses; Type: TABLE; Schema: public; Owner: san0kq
--

CREATE TABLE public.adresses (
    id integer NOT NULL,
    city_id integer NOT NULL,
    street character varying(30) NOT NULL,
    house_number smallint NOT NULL,
    office_number smallint
);


ALTER TABLE public.adresses OWNER TO san0kq;

--
-- Name: adresses_id_seq; Type: SEQUENCE; Schema: public; Owner: san0kq
--

CREATE SEQUENCE public.adresses_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.adresses_id_seq OWNER TO san0kq;

--
-- Name: adresses_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: san0kq
--

ALTER SEQUENCE public.adresses_id_seq OWNED BY public.adresses.id;


--
-- Name: cities; Type: TABLE; Schema: public; Owner: san0kq
--

CREATE TABLE public.cities (
    id integer NOT NULL,
    name character varying(50) NOT NULL,
    country_name character varying(50) NOT NULL
);


ALTER TABLE public.cities OWNER TO san0kq;

--
-- Name: cities_id_seq; Type: SEQUENCE; Schema: public; Owner: san0kq
--

CREATE SEQUENCE public.cities_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.cities_id_seq OWNER TO san0kq;

--
-- Name: cities_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: san0kq
--

ALTER SEQUENCE public.cities_id_seq OWNED BY public.cities.id;


--
-- Name: companies; Type: TABLE; Schema: public; Owner: san0kq
--

CREATE TABLE public.companies (
    id integer NOT NULL,
    name character varying(150) NOT NULL,
    employees_number_size_range character varying(30),
    founded_in smallint NOT NULL,
    logo text NOT NULL,
    description text NOT NULL,
    email character varying(254) NOT NULL,
    phone_number character varying(20) NOT NULL,
    web_site text NOT NULL,
    adress_id integer NOT NULL,
    registred_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE public.companies OWNER TO san0kq;

--
-- Name: companies_id_seq; Type: SEQUENCE; Schema: public; Owner: san0kq
--

CREATE SEQUENCE public.companies_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.companies_id_seq OWNER TO san0kq;

--
-- Name: companies_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: san0kq
--

ALTER SEQUENCE public.companies_id_seq OWNED BY public.companies.id;


--
-- Name: companies_sectors; Type: TABLE; Schema: public; Owner: san0kq
--

CREATE TABLE public.companies_sectors (
    company_id integer NOT NULL,
    sector_name character varying(30) NOT NULL
);


ALTER TABLE public.companies_sectors OWNER TO san0kq;

--
-- Name: contracts; Type: TABLE; Schema: public; Owner: san0kq
--

CREATE TABLE public.contracts (
    name character varying(40) NOT NULL
);


ALTER TABLE public.contracts OWNER TO san0kq;

--
-- Name: countries; Type: TABLE; Schema: public; Owner: san0kq
--

CREATE TABLE public.countries (
    name character varying(50) NOT NULL
);


ALTER TABLE public.countries OWNER TO san0kq;

--
-- Name: employees; Type: TABLE; Schema: public; Owner: san0kq
--

CREATE TABLE public.employees (
    id integer NOT NULL,
    first_name character varying(255) NOT NULL,
    last_name character varying(255) NOT NULL,
    company_id integer NOT NULL,
    email character varying(254) NOT NULL,
    phone_number character varying(20) NOT NULL,
    password character varying(35) NOT NULL,
    city_id integer,
    image text NOT NULL,
    registred_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE public.employees OWNER TO san0kq;

--
-- Name: employees_id_seq; Type: SEQUENCE; Schema: public; Owner: san0kq
--

CREATE SEQUENCE public.employees_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.employees_id_seq OWNER TO san0kq;

--
-- Name: employees_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: san0kq
--

ALTER SEQUENCE public.employees_id_seq OWNED BY public.employees.id;


--
-- Name: employees_numbers; Type: TABLE; Schema: public; Owner: san0kq
--

CREATE TABLE public.employees_numbers (
    size_range character varying(30) NOT NULL
);


ALTER TABLE public.employees_numbers OWNER TO san0kq;

--
-- Name: employees_positions; Type: TABLE; Schema: public; Owner: san0kq
--

CREATE TABLE public.employees_positions (
    employee_id integer NOT NULL,
    position_name character varying(100) NOT NULL
);


ALTER TABLE public.employees_positions OWNER TO san0kq;

--
-- Name: genders; Type: TABLE; Schema: public; Owner: san0kq
--

CREATE TABLE public.genders (
    name character varying(30) NOT NULL
);


ALTER TABLE public.genders OWNER TO san0kq;

--
-- Name: language_levels; Type: TABLE; Schema: public; Owner: san0kq
--

CREATE TABLE public.language_levels (
    name character varying(30) NOT NULL
);


ALTER TABLE public.language_levels OWNER TO san0kq;

--
-- Name: languages; Type: TABLE; Schema: public; Owner: san0kq
--

CREATE TABLE public.languages (
    name character varying(30) NOT NULL
);


ALTER TABLE public.languages OWNER TO san0kq;

--
-- Name: levels; Type: TABLE; Schema: public; Owner: san0kq
--

CREATE TABLE public.levels (
    name character varying(40) NOT NULL
);


ALTER TABLE public.levels OWNER TO san0kq;

--
-- Name: positions; Type: TABLE; Schema: public; Owner: san0kq
--

CREATE TABLE public.positions (
    name character varying(100) NOT NULL
);


ALTER TABLE public.positions OWNER TO san0kq;

--
-- Name: profiles; Type: TABLE; Schema: public; Owner: san0kq
--

CREATE TABLE public.profiles (
    id integer NOT NULL,
    phone_number character varying(20) NOT NULL,
    age smallint NOT NULL,
    gender_name character varying(30),
    city_id integer,
    image text NOT NULL,
    resume text NOT NULL,
    years_exp smallint,
    status_name character varying(30) DEFAULT 'open to work'::character varying,
    work_format_name character varying(50),
    level_name character varying(40),
    contract_name character varying(40),
    min_salary numeric(10,2),
    max_salary numeric(10,2),
    CONSTRAINT profiles_age_check CHECK (((age >= 15) AND (age <= 121))),
    CONSTRAINT profiles_years_exp_check CHECK (((years_exp >= '-1'::integer) AND (years_exp <= 120)))
);


ALTER TABLE public.profiles OWNER TO san0kq;

--
-- Name: profiles_id_seq; Type: SEQUENCE; Schema: public; Owner: san0kq
--

CREATE SEQUENCE public.profiles_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.profiles_id_seq OWNER TO san0kq;

--
-- Name: profiles_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: san0kq
--

ALTER SEQUENCE public.profiles_id_seq OWNED BY public.profiles.id;


--
-- Name: profiles_languages; Type: TABLE; Schema: public; Owner: san0kq
--

CREATE TABLE public.profiles_languages (
    profile_id integer NOT NULL,
    language_name character varying(30) NOT NULL,
    language_lvl_name character varying(30) NOT NULL
);


ALTER TABLE public.profiles_languages OWNER TO san0kq;

--
-- Name: profiles_tags; Type: TABLE; Schema: public; Owner: san0kq
--

CREATE TABLE public.profiles_tags (
    profile_id integer NOT NULL,
    tag_name character varying(30) NOT NULL
);


ALTER TABLE public.profiles_tags OWNER TO san0kq;

--
-- Name: ratings; Type: TABLE; Schema: public; Owner: san0kq
--

CREATE TABLE public.ratings (
    name character varying(20) NOT NULL
);


ALTER TABLE public.ratings OWNER TO san0kq;

--
-- Name: responses; Type: TABLE; Schema: public; Owner: san0kq
--

CREATE TABLE public.responses (
    id integer NOT NULL,
    user_id integer NOT NULL,
    vacancy_id integer NOT NULL,
    text character varying(500) NOT NULL,
    phone_number character varying(20) NOT NULL,
    status_name character varying(30) DEFAULT 'created'::character varying,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE public.responses OWNER TO san0kq;

--
-- Name: responses_id_seq; Type: SEQUENCE; Schema: public; Owner: san0kq
--

CREATE SEQUENCE public.responses_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.responses_id_seq OWNER TO san0kq;

--
-- Name: responses_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: san0kq
--

ALTER SEQUENCE public.responses_id_seq OWNED BY public.responses.id;


--
-- Name: review_ratings; Type: TABLE; Schema: public; Owner: san0kq
--

CREATE TABLE public.review_ratings (
    review_id integer NOT NULL,
    user_id integer NOT NULL,
    rating_name character varying(20) NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE public.review_ratings OWNER TO san0kq;

--
-- Name: reviews; Type: TABLE; Schema: public; Owner: san0kq
--

CREATE TABLE public.reviews (
    id integer NOT NULL,
    text character varying(800) NOT NULL,
    user_id integer NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE public.reviews OWNER TO san0kq;

--
-- Name: reviews_id_seq; Type: SEQUENCE; Schema: public; Owner: san0kq
--

CREATE SEQUENCE public.reviews_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.reviews_id_seq OWNER TO san0kq;

--
-- Name: reviews_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: san0kq
--

ALTER SEQUENCE public.reviews_id_seq OWNED BY public.reviews.id;


--
-- Name: sectors; Type: TABLE; Schema: public; Owner: san0kq
--

CREATE TABLE public.sectors (
    name character varying(30) NOT NULL
);


ALTER TABLE public.sectors OWNER TO san0kq;

--
-- Name: social_links; Type: TABLE; Schema: public; Owner: san0kq
--

CREATE TABLE public.social_links (
    id integer NOT NULL,
    platform character varying(100) NOT NULL,
    url text NOT NULL,
    profile_id integer,
    company_id integer
);


ALTER TABLE public.social_links OWNER TO san0kq;

--
-- Name: social_links_id_seq; Type: SEQUENCE; Schema: public; Owner: san0kq
--

CREATE SEQUENCE public.social_links_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.social_links_id_seq OWNER TO san0kq;

--
-- Name: social_links_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: san0kq
--

ALTER SEQUENCE public.social_links_id_seq OWNED BY public.social_links.id;


--
-- Name: statuses; Type: TABLE; Schema: public; Owner: san0kq
--

CREATE TABLE public.statuses (
    name character varying(30) NOT NULL
);


ALTER TABLE public.statuses OWNER TO san0kq;

--
-- Name: tags; Type: TABLE; Schema: public; Owner: san0kq
--

CREATE TABLE public.tags (
    name character varying(30) NOT NULL
);


ALTER TABLE public.tags OWNER TO san0kq;

--
-- Name: users; Type: TABLE; Schema: public; Owner: san0kq
--

CREATE TABLE public.users (
    id integer NOT NULL,
    username character varying(20) NOT NULL,
    password character varying(35) NOT NULL,
    email character varying(254) NOT NULL,
    first_name character varying(255) NOT NULL,
    last_name character varying(255) NOT NULL,
    registred_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    is_active boolean DEFAULT true,
    profile_id integer NOT NULL
);


ALTER TABLE public.users OWNER TO san0kq;

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: san0kq
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_id_seq OWNER TO san0kq;

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: san0kq
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: vacancies; Type: TABLE; Schema: public; Owner: san0kq
--

CREATE TABLE public.vacancies (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    employee_id integer NOT NULL,
    description text NOT NULL,
    min_salary numeric(10,2),
    max_salary numeric(10,2),
    company_id integer NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE public.vacancies OWNER TO san0kq;

--
-- Name: vacancies_contracts; Type: TABLE; Schema: public; Owner: san0kq
--

CREATE TABLE public.vacancies_contracts (
    vacancy_id integer NOT NULL,
    contract_name character varying(40) NOT NULL
);


ALTER TABLE public.vacancies_contracts OWNER TO san0kq;

--
-- Name: vacancies_countries; Type: TABLE; Schema: public; Owner: san0kq
--

CREATE TABLE public.vacancies_countries (
    vacancy_id integer NOT NULL,
    country_name character varying(50) NOT NULL
);


ALTER TABLE public.vacancies_countries OWNER TO san0kq;

--
-- Name: vacancies_id_seq; Type: SEQUENCE; Schema: public; Owner: san0kq
--

CREATE SEQUENCE public.vacancies_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.vacancies_id_seq OWNER TO san0kq;

--
-- Name: vacancies_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: san0kq
--

ALTER SEQUENCE public.vacancies_id_seq OWNED BY public.vacancies.id;


--
-- Name: vacancies_levels; Type: TABLE; Schema: public; Owner: san0kq
--

CREATE TABLE public.vacancies_levels (
    vacancy_id integer NOT NULL,
    level_name character varying(40) NOT NULL
);


ALTER TABLE public.vacancies_levels OWNER TO san0kq;

--
-- Name: vacancies_tags; Type: TABLE; Schema: public; Owner: san0kq
--

CREATE TABLE public.vacancies_tags (
    vacancy_id integer NOT NULL,
    tag_name character varying(30) NOT NULL
);


ALTER TABLE public.vacancies_tags OWNER TO san0kq;

--
-- Name: vacancies_work_formats; Type: TABLE; Schema: public; Owner: san0kq
--

CREATE TABLE public.vacancies_work_formats (
    vacancy_id integer NOT NULL,
    work_format_name character varying(50) NOT NULL
);


ALTER TABLE public.vacancies_work_formats OWNER TO san0kq;

--
-- Name: work_formats; Type: TABLE; Schema: public; Owner: san0kq
--

CREATE TABLE public.work_formats (
    name character varying(50) NOT NULL
);


ALTER TABLE public.work_formats OWNER TO san0kq;

--
-- Name: adresses id; Type: DEFAULT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.adresses ALTER COLUMN id SET DEFAULT nextval('public.adresses_id_seq'::regclass);


--
-- Name: cities id; Type: DEFAULT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.cities ALTER COLUMN id SET DEFAULT nextval('public.cities_id_seq'::regclass);


--
-- Name: companies id; Type: DEFAULT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.companies ALTER COLUMN id SET DEFAULT nextval('public.companies_id_seq'::regclass);


--
-- Name: employees id; Type: DEFAULT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.employees ALTER COLUMN id SET DEFAULT nextval('public.employees_id_seq'::regclass);


--
-- Name: profiles id; Type: DEFAULT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.profiles ALTER COLUMN id SET DEFAULT nextval('public.profiles_id_seq'::regclass);


--
-- Name: responses id; Type: DEFAULT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.responses ALTER COLUMN id SET DEFAULT nextval('public.responses_id_seq'::regclass);


--
-- Name: reviews id; Type: DEFAULT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.reviews ALTER COLUMN id SET DEFAULT nextval('public.reviews_id_seq'::regclass);


--
-- Name: social_links id; Type: DEFAULT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.social_links ALTER COLUMN id SET DEFAULT nextval('public.social_links_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Name: vacancies id; Type: DEFAULT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.vacancies ALTER COLUMN id SET DEFAULT nextval('public.vacancies_id_seq'::regclass);


--
-- Name: adresses adresses_pkey; Type: CONSTRAINT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.adresses
    ADD CONSTRAINT adresses_pkey PRIMARY KEY (id);


--
-- Name: cities cities_pkey; Type: CONSTRAINT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.cities
    ADD CONSTRAINT cities_pkey PRIMARY KEY (id);


--
-- Name: companies companies_adress_id_key; Type: CONSTRAINT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.companies
    ADD CONSTRAINT companies_adress_id_key UNIQUE (adress_id);


--
-- Name: companies companies_name_key; Type: CONSTRAINT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.companies
    ADD CONSTRAINT companies_name_key UNIQUE (name);


--
-- Name: companies companies_pkey; Type: CONSTRAINT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.companies
    ADD CONSTRAINT companies_pkey PRIMARY KEY (id);


--
-- Name: companies_sectors companies_sectors_pkey; Type: CONSTRAINT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.companies_sectors
    ADD CONSTRAINT companies_sectors_pkey PRIMARY KEY (company_id, sector_name);


--
-- Name: contracts contracts_pkey; Type: CONSTRAINT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.contracts
    ADD CONSTRAINT contracts_pkey PRIMARY KEY (name);


--
-- Name: countries countries_pkey; Type: CONSTRAINT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.countries
    ADD CONSTRAINT countries_pkey PRIMARY KEY (name);


--
-- Name: employees employees_email_key; Type: CONSTRAINT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.employees
    ADD CONSTRAINT employees_email_key UNIQUE (email);


--
-- Name: employees_numbers employees_numbers_pkey; Type: CONSTRAINT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.employees_numbers
    ADD CONSTRAINT employees_numbers_pkey PRIMARY KEY (size_range);


--
-- Name: employees employees_pkey; Type: CONSTRAINT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.employees
    ADD CONSTRAINT employees_pkey PRIMARY KEY (id);


--
-- Name: employees_positions employees_positions_pkey; Type: CONSTRAINT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.employees_positions
    ADD CONSTRAINT employees_positions_pkey PRIMARY KEY (employee_id, position_name);


--
-- Name: genders genders_pkey; Type: CONSTRAINT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.genders
    ADD CONSTRAINT genders_pkey PRIMARY KEY (name);


--
-- Name: language_levels language_levels_pkey; Type: CONSTRAINT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.language_levels
    ADD CONSTRAINT language_levels_pkey PRIMARY KEY (name);


--
-- Name: languages languages_pkey; Type: CONSTRAINT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.languages
    ADD CONSTRAINT languages_pkey PRIMARY KEY (name);


--
-- Name: levels levels_pkey; Type: CONSTRAINT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.levels
    ADD CONSTRAINT levels_pkey PRIMARY KEY (name);


--
-- Name: positions positions_pkey; Type: CONSTRAINT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.positions
    ADD CONSTRAINT positions_pkey PRIMARY KEY (name);


--
-- Name: profiles_languages profiles_languages_pkey; Type: CONSTRAINT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.profiles_languages
    ADD CONSTRAINT profiles_languages_pkey PRIMARY KEY (profile_id, language_name);


--
-- Name: profiles profiles_pkey; Type: CONSTRAINT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.profiles
    ADD CONSTRAINT profiles_pkey PRIMARY KEY (id);


--
-- Name: profiles_tags profiles_tags_pkey; Type: CONSTRAINT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.profiles_tags
    ADD CONSTRAINT profiles_tags_pkey PRIMARY KEY (profile_id, tag_name);


--
-- Name: ratings ratings_pkey; Type: CONSTRAINT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.ratings
    ADD CONSTRAINT ratings_pkey PRIMARY KEY (name);


--
-- Name: responses responses_pkey; Type: CONSTRAINT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.responses
    ADD CONSTRAINT responses_pkey PRIMARY KEY (id);


--
-- Name: review_ratings review_ratings_pkey; Type: CONSTRAINT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.review_ratings
    ADD CONSTRAINT review_ratings_pkey PRIMARY KEY (review_id, user_id);


--
-- Name: reviews reviews_pkey; Type: CONSTRAINT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.reviews
    ADD CONSTRAINT reviews_pkey PRIMARY KEY (id);


--
-- Name: sectors sectors_pkey; Type: CONSTRAINT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.sectors
    ADD CONSTRAINT sectors_pkey PRIMARY KEY (name);


--
-- Name: social_links social_links_pkey; Type: CONSTRAINT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.social_links
    ADD CONSTRAINT social_links_pkey PRIMARY KEY (id);


--
-- Name: social_links social_links_url_key; Type: CONSTRAINT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.social_links
    ADD CONSTRAINT social_links_url_key UNIQUE (url);


--
-- Name: statuses statuses_pkey; Type: CONSTRAINT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.statuses
    ADD CONSTRAINT statuses_pkey PRIMARY KEY (name);


--
-- Name: tags tags_pkey; Type: CONSTRAINT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.tags
    ADD CONSTRAINT tags_pkey PRIMARY KEY (name);


--
-- Name: users users_email_key; Type: CONSTRAINT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_email_key UNIQUE (email);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: users users_profile_id_key; Type: CONSTRAINT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_profile_id_key UNIQUE (profile_id);


--
-- Name: users users_username_key; Type: CONSTRAINT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_username_key UNIQUE (username);


--
-- Name: vacancies_contracts vacancies_contracts_pkey; Type: CONSTRAINT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.vacancies_contracts
    ADD CONSTRAINT vacancies_contracts_pkey PRIMARY KEY (vacancy_id, contract_name);


--
-- Name: vacancies_countries vacancies_countries_pkey; Type: CONSTRAINT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.vacancies_countries
    ADD CONSTRAINT vacancies_countries_pkey PRIMARY KEY (vacancy_id, country_name);


--
-- Name: vacancies_levels vacancies_levels_pkey; Type: CONSTRAINT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.vacancies_levels
    ADD CONSTRAINT vacancies_levels_pkey PRIMARY KEY (vacancy_id, level_name);


--
-- Name: vacancies vacancies_pkey; Type: CONSTRAINT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.vacancies
    ADD CONSTRAINT vacancies_pkey PRIMARY KEY (id);


--
-- Name: vacancies_tags vacancies_tags_pkey; Type: CONSTRAINT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.vacancies_tags
    ADD CONSTRAINT vacancies_tags_pkey PRIMARY KEY (vacancy_id, tag_name);


--
-- Name: vacancies_work_formats vacancies_work_formats_pkey; Type: CONSTRAINT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.vacancies_work_formats
    ADD CONSTRAINT vacancies_work_formats_pkey PRIMARY KEY (vacancy_id, work_format_name);


--
-- Name: work_formats work_formats_pkey; Type: CONSTRAINT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.work_formats
    ADD CONSTRAINT work_formats_pkey PRIMARY KEY (name);


--
-- Name: adresses adresses_city_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.adresses
    ADD CONSTRAINT adresses_city_id_fkey FOREIGN KEY (city_id) REFERENCES public.cities(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: cities cities_country_name_fkey; Type: FK CONSTRAINT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.cities
    ADD CONSTRAINT cities_country_name_fkey FOREIGN KEY (country_name) REFERENCES public.countries(name) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: companies companies_adress_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.companies
    ADD CONSTRAINT companies_adress_id_fkey FOREIGN KEY (adress_id) REFERENCES public.adresses(id) ON UPDATE CASCADE ON DELETE SET NULL;


--
-- Name: companies companies_employees_number_size_range_fkey; Type: FK CONSTRAINT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.companies
    ADD CONSTRAINT companies_employees_number_size_range_fkey FOREIGN KEY (employees_number_size_range) REFERENCES public.employees_numbers(size_range) ON UPDATE CASCADE ON DELETE SET NULL;


--
-- Name: companies_sectors companies_sectors_company_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.companies_sectors
    ADD CONSTRAINT companies_sectors_company_id_fkey FOREIGN KEY (company_id) REFERENCES public.companies(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: companies_sectors companies_sectors_sector_name_fkey; Type: FK CONSTRAINT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.companies_sectors
    ADD CONSTRAINT companies_sectors_sector_name_fkey FOREIGN KEY (sector_name) REFERENCES public.sectors(name) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: employees employees_city_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.employees
    ADD CONSTRAINT employees_city_id_fkey FOREIGN KEY (city_id) REFERENCES public.cities(id) ON UPDATE CASCADE ON DELETE SET NULL;


--
-- Name: employees employees_company_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.employees
    ADD CONSTRAINT employees_company_id_fkey FOREIGN KEY (company_id) REFERENCES public.companies(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: employees_positions employees_positions_employee_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.employees_positions
    ADD CONSTRAINT employees_positions_employee_id_fkey FOREIGN KEY (employee_id) REFERENCES public.employees(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: employees_positions employees_positions_position_name_fkey; Type: FK CONSTRAINT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.employees_positions
    ADD CONSTRAINT employees_positions_position_name_fkey FOREIGN KEY (position_name) REFERENCES public.positions(name) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: profiles profiles_city_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.profiles
    ADD CONSTRAINT profiles_city_id_fkey FOREIGN KEY (city_id) REFERENCES public.cities(id) ON UPDATE CASCADE ON DELETE SET NULL;


--
-- Name: profiles profiles_contract_name_fkey; Type: FK CONSTRAINT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.profiles
    ADD CONSTRAINT profiles_contract_name_fkey FOREIGN KEY (contract_name) REFERENCES public.contracts(name) ON UPDATE CASCADE ON DELETE SET NULL;


--
-- Name: profiles profiles_gender_name_fkey; Type: FK CONSTRAINT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.profiles
    ADD CONSTRAINT profiles_gender_name_fkey FOREIGN KEY (gender_name) REFERENCES public.genders(name) ON UPDATE CASCADE ON DELETE SET NULL;


--
-- Name: profiles_languages profiles_languages_language_lvl_name_fkey; Type: FK CONSTRAINT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.profiles_languages
    ADD CONSTRAINT profiles_languages_language_lvl_name_fkey FOREIGN KEY (language_lvl_name) REFERENCES public.language_levels(name) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: profiles_languages profiles_languages_language_name_fkey; Type: FK CONSTRAINT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.profiles_languages
    ADD CONSTRAINT profiles_languages_language_name_fkey FOREIGN KEY (language_name) REFERENCES public.languages(name) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: profiles_languages profiles_languages_profile_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.profiles_languages
    ADD CONSTRAINT profiles_languages_profile_id_fkey FOREIGN KEY (profile_id) REFERENCES public.profiles(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: profiles profiles_level_name_fkey; Type: FK CONSTRAINT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.profiles
    ADD CONSTRAINT profiles_level_name_fkey FOREIGN KEY (level_name) REFERENCES public.levels(name) ON UPDATE CASCADE ON DELETE SET NULL;


--
-- Name: profiles profiles_status_name_fkey; Type: FK CONSTRAINT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.profiles
    ADD CONSTRAINT profiles_status_name_fkey FOREIGN KEY (status_name) REFERENCES public.statuses(name) ON UPDATE CASCADE ON DELETE SET NULL;


--
-- Name: profiles_tags profiles_tags_profile_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.profiles_tags
    ADD CONSTRAINT profiles_tags_profile_id_fkey FOREIGN KEY (profile_id) REFERENCES public.profiles(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: profiles_tags profiles_tags_tag_name_fkey; Type: FK CONSTRAINT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.profiles_tags
    ADD CONSTRAINT profiles_tags_tag_name_fkey FOREIGN KEY (tag_name) REFERENCES public.tags(name) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: profiles profiles_work_format_name_fkey; Type: FK CONSTRAINT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.profiles
    ADD CONSTRAINT profiles_work_format_name_fkey FOREIGN KEY (work_format_name) REFERENCES public.work_formats(name) ON UPDATE CASCADE ON DELETE SET NULL;


--
-- Name: responses responses_status_name_fkey; Type: FK CONSTRAINT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.responses
    ADD CONSTRAINT responses_status_name_fkey FOREIGN KEY (status_name) REFERENCES public.statuses(name) ON UPDATE CASCADE ON DELETE SET NULL;


--
-- Name: responses responses_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.responses
    ADD CONSTRAINT responses_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: responses responses_vacancy_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.responses
    ADD CONSTRAINT responses_vacancy_id_fkey FOREIGN KEY (vacancy_id) REFERENCES public.vacancies(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: review_ratings review_ratings_review_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.review_ratings
    ADD CONSTRAINT review_ratings_review_id_fkey FOREIGN KEY (review_id) REFERENCES public.reviews(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: review_ratings review_ratings_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.review_ratings
    ADD CONSTRAINT review_ratings_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: reviews reviews_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.reviews
    ADD CONSTRAINT reviews_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: social_links social_links_company_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.social_links
    ADD CONSTRAINT social_links_company_id_fkey FOREIGN KEY (company_id) REFERENCES public.companies(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: social_links social_links_profile_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.social_links
    ADD CONSTRAINT social_links_profile_id_fkey FOREIGN KEY (profile_id) REFERENCES public.profiles(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: users users_profile_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_profile_id_fkey FOREIGN KEY (profile_id) REFERENCES public.profiles(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: vacancies vacancies_company_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.vacancies
    ADD CONSTRAINT vacancies_company_id_fkey FOREIGN KEY (company_id) REFERENCES public.companies(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: vacancies_contracts vacancies_contracts_contract_name_fkey; Type: FK CONSTRAINT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.vacancies_contracts
    ADD CONSTRAINT vacancies_contracts_contract_name_fkey FOREIGN KEY (contract_name) REFERENCES public.contracts(name) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: vacancies_contracts vacancies_contracts_vacancy_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.vacancies_contracts
    ADD CONSTRAINT vacancies_contracts_vacancy_id_fkey FOREIGN KEY (vacancy_id) REFERENCES public.vacancies(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: vacancies_countries vacancies_countries_country_name_fkey; Type: FK CONSTRAINT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.vacancies_countries
    ADD CONSTRAINT vacancies_countries_country_name_fkey FOREIGN KEY (country_name) REFERENCES public.countries(name) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: vacancies_countries vacancies_countries_vacancy_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.vacancies_countries
    ADD CONSTRAINT vacancies_countries_vacancy_id_fkey FOREIGN KEY (vacancy_id) REFERENCES public.vacancies(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: vacancies vacancies_employee_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.vacancies
    ADD CONSTRAINT vacancies_employee_id_fkey FOREIGN KEY (employee_id) REFERENCES public.employees(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: vacancies_levels vacancies_levels_level_name_fkey; Type: FK CONSTRAINT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.vacancies_levels
    ADD CONSTRAINT vacancies_levels_level_name_fkey FOREIGN KEY (level_name) REFERENCES public.levels(name) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: vacancies_levels vacancies_levels_vacancy_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.vacancies_levels
    ADD CONSTRAINT vacancies_levels_vacancy_id_fkey FOREIGN KEY (vacancy_id) REFERENCES public.vacancies(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: vacancies_tags vacancies_tags_tag_name_fkey; Type: FK CONSTRAINT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.vacancies_tags
    ADD CONSTRAINT vacancies_tags_tag_name_fkey FOREIGN KEY (tag_name) REFERENCES public.tags(name) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: vacancies_tags vacancies_tags_vacancy_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.vacancies_tags
    ADD CONSTRAINT vacancies_tags_vacancy_id_fkey FOREIGN KEY (vacancy_id) REFERENCES public.vacancies(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: vacancies_work_formats vacancies_work_formats_vacancy_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.vacancies_work_formats
    ADD CONSTRAINT vacancies_work_formats_vacancy_id_fkey FOREIGN KEY (vacancy_id) REFERENCES public.vacancies(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: vacancies_work_formats vacancies_work_formats_work_format_name_fkey; Type: FK CONSTRAINT; Schema: public; Owner: san0kq
--

ALTER TABLE ONLY public.vacancies_work_formats
    ADD CONSTRAINT vacancies_work_formats_work_format_name_fkey FOREIGN KEY (work_format_name) REFERENCES public.work_formats(name) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- PostgreSQL database dump complete
--

