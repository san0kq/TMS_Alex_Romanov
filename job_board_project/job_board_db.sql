CREATE TABLE genders (
    name VARCHAR(30) PRIMARY KEY
);
CREATE TABLE languages (
    name VARCHAR(30) PRIMARY KEY
);
CREATE TABLE language_levels (
    name VARCHAR(30) PRIMARY KEY
);
CREATE TABLE ratings (
    name VARCHAR(20) PRIMARY KEY
);
CREATE TABLE positions (
    name VARCHAR(100) PRIMARY KEY
);
CREATE TABLE work_formats (
    name VARCHAR(50) PRIMARY KEY
);
CREATE TABLE statuses (
    name VARCHAR(30) PRIMARY KEY
);
CREATE TABLE countries (
    name VARCHAR(50) PRIMARY KEY
);
CREATE TABLE tags (
    name VARCHAR(30) PRIMARY KEY
);
CREATE TABLE cities (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    country_name VARCHAR(50) NOT NULL,
    FOREIGN KEY (country_name) REFERENCES countries(name) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE contracts (
    name VARCHAR(40) PRIMARY KEY
);
CREATE TABLE levels (
    name VARCHAR(40) PRIMARY KEY
);
CREATE TABLE salaries (
    id SERIAL PRIMARY KEY,
    min_salary NUMERIC(10, 2),
    max_salary NUMERIC(10, 2),
    UNIQUE(min_salary, max_salary)
);
CREATE TABLE adresses (
    id SERIAL PRIMARY KEY,
    city_id INTEGER NOT NULL,
    street VARCHAR(30) NOT NULL,
    house_number SMALLINT NOT NULL,
    office_number SMALLINT,
    FOREIGN KEY (city_id) REFERENCES cities(id) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE employees_numbers (
    size_range VARCHAR(30) PRIMARY KEY
);
CREATE TABLE sectors (
    name VARCHAR(30) PRIMARY KEY
);
CREATE TABLE companies (
    id SERIAL PRIMARY KEY,
    name VARCHAR(150) UNIQUE NOT NULL,
    employees_number_size_range VARCHAR(30),
    founded_in SMALLINT NOT NULL,
    logo TEXT NOT NULL,
    description TEXT NOT NULL,
    email VARCHAR(254) NOT NULL,
    phone_number VARCHAR(20) NOT NULL,
    web_site TEXT NOT NULL,
    adress_id INTEGER UNIQUE,
    registred_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (employees_number_size_range) REFERENCES employees_numbers(size_range) ON DELETE SET NULL ON UPDATE CASCADE,
    FOREIGN KEY (adress_id) REFERENCES adresses(id) ON DELETE SET NULL ON UPDATE CASCADE
);
CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    company_id INTEGER NOT NULL,
    email VARCHAR(254) UNIQUE NOT NULL,
    phone_number VARCHAR(20) NOT NULL,
    password VARCHAR(35) NOT NULL,
    city_id INTEGER,
    image TEXT NOT NULL,
    registred_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (company_id) REFERENCES companies(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (city_id) REFERENCES cities(id) ON DELETE SET NULL ON UPDATE CASCADE
);
CREATE TABLE vacancies (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    employee_id INTEGER NOT NULL,
    description TEXT NOT NULL,
    salary_id INTEGER,
    company_id INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (employee_id) REFERENCES employees(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (salary_id) REFERENCES salaries(id) ON DELETE SET NULL ON UPDATE CASCADE,
    FOREIGN KEY (company_id) REFERENCES companies(id) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE profiles (
    id SERIAL PRIMARY KEY,
    phone_number VARCHAR(20) NOT NULL,
    age SMALLINT CHECK (age BETWEEN 15 AND 121) NOT NULL,
    gender_name VARCHAR(30),
    city_id INTEGER,
    image TEXT NOT NULL,
    resume TEXT NOT NULL,
    years_exp SMALLINT CHECK (years_exp BETWEEN -1 AND 120),
    status_name VARCHAR(30) DEFAULT 'open to work',
    work_format_name VARCHAR(50),
    level_name VARCHAR(40),
    contract_name VARCHAR(40),
    salary_id INTEGER,
    FOREIGN KEY (gender_name) REFERENCES genders(name) ON DELETE SET NULL ON UPDATE CASCADE,
    FOREIGN KEY (city_id) REFERENCES cities(id) ON DELETE SET NULL ON UPDATE CASCADE,
    FOREIGN KEY (status_name) REFERENCES statuses(name) ON DELETE SET NULL ON UPDATE CASCADE,
    FOREIGN KEY (work_format_name) REFERENCES work_formats(name) ON DELETE SET NULL ON UPDATE CASCADE,
    FOREIGN KEY (level_name) REFERENCES levels(name) ON DELETE SET NULL ON UPDATE CASCADE,
    FOREIGN KEY (contract_name) REFERENCES contracts(name) ON DELETE SET NULL ON UPDATE CASCADE,
    FOREIGN KEY (salary_id) REFERENCES salaries(id) ON DELETE SET NULL ON UPDATE CASCADE
);
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(20) UNIQUE NOT NULL,
    password VARCHAR(35) NOT NULL,
    email VARCHAR(254) UNIQUE NOT NULL,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    registred_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE,
    profile_id INTEGER UNIQUE NOT NULL,
    FOREIGN KEY (profile_id) REFERENCES profiles(id) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE profile_languages (
    profile_id INTEGER,
    language_name VARCHAR(30),
    language_lvl_name VARCHAR(30) NOT NULL,
    PRIMARY KEY (profile_id, language_name),
    FOREIGN KEY (profile_id) REFERENCES profiles(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (language_name) REFERENCES languages(name) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (language_lvl_name) REFERENCES language_levels(name) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE reviews (
    id SERIAL PRIMARY KEY,
    text VARCHAR(800) NOT NULL,
    user_id INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE review_ratings (
    review_id INTEGER,
    user_id INTEGER,
    rating_name VARCHAR(20) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (review_id, user_id),
    FOREIGN KEY (review_id) REFERENCES reviews(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (rating_name) REFERENCES ratings(name) ON DELETE CASCADE ON UPDATE CASCADE 
);
CREATE TABLE social_links (
    id SERIAL PRIMARY KEY,
    platform VARCHAR(100) NOT NULL,
    url TEXT UNIQUE NOT NULL,
    profile_id INTEGER,
    company_id INTEGER,
    FOREIGN KEY (profile_id) REFERENCES profiles(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (company_id) REFERENCES companies(id) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE responses (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    vacancy_id INTEGER NOT NULL,
    text VARCHAR(500) NOT NULL,
    phone_number VARCHAR(20) NOT NULL,
    status_name VARCHAR(30) DEFAULT 'created',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (vacancy_id) REFERENCES vacancies(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (status_name) REFERENCES statuses(name) ON DELETE SET NULL ON UPDATE CASCADE
);
CREATE TABLE profiles_tags (
    profile_id INTEGER,
    tag_name VARCHAR(30),
    PRIMARY KEY (profile_id, tag_name),
    FOREIGN KEY (profile_id) REFERENCES profiles(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (tag_name) REFERENCES tags(name) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE employees_positions (
    employee_id INTEGER,
    position_name VARCHAR(100),
    PRIMARY KEY (employee_id, position_name),
    FOREIGN KEY (employee_id) REFERENCES employees(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (position_name) REFERENCES positions(name) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE companies_sectors (
    company_id INTEGER,
    sector_name VARCHAR(30),
    PRIMARY KEY (company_id, sector_name),
    FOREIGN KEY (company_id) REFERENCES companies(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (sector_name) REFERENCES sectors(name) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE vacancies_countries (
    vacancy_id INTEGER,
    country_name VARCHAR(50),
    PRIMARY KEY (vacancy_id, country_name),
    FOREIGN KEY (vacancy_id) REFERENCES vacancies(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (country_name) REFERENCES countries(name) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE vacancies_tags (
    vacancy_id INTEGER,
    tag_name VARCHAR(30),
    PRIMARY KEY (vacancy_id, tag_name),
    FOREIGN KEY (vacancy_id) REFERENCES vacancies(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (tag_name) REFERENCES tags(name) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE vacancies_contracts (
    vacancy_id INTEGER,
    contract_name VARCHAR(40),
    PRIMARY KEY (vacancy_id, contract_name),
    FOREIGN KEY (vacancy_id) REFERENCES vacancies(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (contract_name) REFERENCES contracts(name) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE vacancies_levels (
    vacancy_id INTEGER,
    level_name VARCHAR(40),
    PRIMARY KEY (vacancy_id, level_name),
    FOREIGN KEY (vacancy_id) REFERENCES vacancies(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (level_name) REFERENCES levels(name) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE vacancies_work_formats (
    vacancy_id INTEGER,
    work_format_name VARCHAR(50),
    PRIMARY KEY (vacancy_id, work_format_name),
    FOREIGN KEY (vacancy_id) REFERENCES vacancies(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (work_format_name) REFERENCES work_formats(name) ON DELETE CASCADE ON UPDATE CASCADE
);
