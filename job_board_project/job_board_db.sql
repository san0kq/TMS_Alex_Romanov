CREATE TABLE genders (
    id SERIAL PRIMARY KEY,
    name VARCHAR(30) UNIQUE NOT NULL
);
CREATE TABLE languages (
    id SERIAL PRIMARY KEY,
    name VARCHAR(30) UNIQUE NOT NULL
);
CREATE TABLE language_levels (
    id SERIAL PRIMARY KEY,
    name VARCHAR(30) UNIQUE NOT NULL
);
CREATE TABLE ratings (
    id SERIAL PRIMARY KEY,
    name VARCHAR(20) UNIQUE NOT NULL
);
CREATE TABLE positions (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) UNIQUE NOT NULL
);
CREATE TABLE work_formats (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL
);
CREATE TABLE statuses (
    id SERIAL PRIMARY KEY,
    name VARCHAR(30) UNIQUE NOT NULL
);
CREATE TABLE countries (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL
);
CREATE TABLE tags (
    id SERIAL PRIMARY KEY,
    name VARCHAR(30) UNIQUE NOT NULL
);
CREATE TABLE cities (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    country_id INTEGER NOT NULL,
    FOREIGN KEY (country_id) REFERENCES countries(id) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE contracts (
    id SERIAL PRIMARY KEY,
    name VARCHAR(40) UNIQUE NOT NULL
);
CREATE TABLE levels (
    id SERIAL PRIMARY KEY,
    name VARCHAR(40) UNIQUE NOT NULL
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
    id SERIAL PRIMARY KEY,
    size_range VARCHAR(30) UNIQUE NOT NULL
);
CREATE TABLE sectors (
    id SERIAL PRIMARY KEY,
    name VARCHAR(30) UNIQUE NOT NULL
);
CREATE TABLE companies (
    id SERIAL PRIMARY KEY,
    name VARCHAR(150) UNIQUE NOT NULL,
    employees_number_id INTEGER,
    founded_in SMALLINT NOT NULL,
    logo TEXT NOT NULL,
    description TEXT NOT NULL,
    email VARCHAR(254) NOT NULL,
    phone_number VARCHAR(20) NOT NULL,
    web_site TEXT NOT NULL,
    adress_id INTEGER UNIQUE,
    registred_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (employees_number_id) REFERENCES employees_numbers(id) ON DELETE SET NULL ON UPDATE CASCADE,
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
    gender_id INTEGER,
    city_id INTEGER,
    image TEXT NOT NULL,
    resume TEXT NOT NULL,
    years_exp SMALLINT CHECK (years_exp BETWEEN -1 AND 120),
    status_id INTEGER DEFAULT 1,
    work_format_id INTEGER,
    level_id INTEGER,
    contract_id INTEGER,
    salary_id INTEGER,
    FOREIGN KEY (gender_id) REFERENCES genders(id) ON DELETE SET NULL ON UPDATE CASCADE,
    FOREIGN KEY (city_id) REFERENCES cities(id) ON DELETE SET NULL ON UPDATE CASCADE,
    FOREIGN KEY (status_id) REFERENCES statuses(id) ON DELETE SET NULL ON UPDATE CASCADE,
    FOREIGN KEY (work_format_id) REFERENCES work_formats(id) ON DELETE SET NULL ON UPDATE CASCADE,
    FOREIGN KEY (level_id) REFERENCES levels(id) ON DELETE SET NULL ON UPDATE CASCADE,
    FOREIGN KEY (contract_id) REFERENCES contracts(id) ON DELETE SET NULL ON UPDATE CASCADE,
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
    id SERIAL PRIMARY KEY,
    profile_id INTEGER NOT NULL,
    language_id INTEGER NOT NULL,
    language_level_id INTEGER NOT NULL,
    UNIQUE (profile_id, language_id),
    FOREIGN KEY (profile_id) REFERENCES profiles(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (language_id) REFERENCES languages(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (language_level_id) REFERENCES language_levels(id) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE reviews (
    id SERIAL PRIMARY KEY,
    text VARCHAR(800) NOT NULL,
    user_id INTEGER NOT NULL,
    company_id INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (user_id, company_id),
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (company_id) REFERENCES companies(id) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE review_ratings (
    id SERIAL PRIMARY KEY,
    review_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    rating_id INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (review_id, user_id),
    FOREIGN KEY (review_id) REFERENCES reviews(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (rating_id) REFERENCES ratings(id) ON DELETE CASCADE ON UPDATE CASCADE 
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
    status_id INTEGER DEFAULT 4,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (vacancy_id) REFERENCES vacancies(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (status_id) REFERENCES statuses(id) ON DELETE SET NULL ON UPDATE CASCADE
);
CREATE TABLE profiles_tags (
    profile_id INTEGER,
    tag_id INTEGER,
    PRIMARY KEY (profile_id, tag_id),
    FOREIGN KEY (profile_id) REFERENCES profiles(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (tag_id) REFERENCES tags(id) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE employees_positions (
    employee_id INTEGER,
    position_id INTEGER,
    PRIMARY KEY (employee_id, position_id),
    FOREIGN KEY (employee_id) REFERENCES employees(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (position_id) REFERENCES positions(id) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE companies_sectors (
    company_id INTEGER,
    sector_id INTEGER,
    PRIMARY KEY (company_id, sector_id),
    FOREIGN KEY (company_id) REFERENCES companies(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (sector_id) REFERENCES sectors(id) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE vacancies_countries (
    vacancy_id INTEGER,
    country_id INTEGER,
    PRIMARY KEY (vacancy_id, country_id),
    FOREIGN KEY (vacancy_id) REFERENCES vacancies(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (country_id) REFERENCES countries(id) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE vacancies_tags (
    vacancy_id INTEGER,
    tag_id INTEGER,
    PRIMARY KEY (vacancy_id, tag_id),
    FOREIGN KEY (vacancy_id) REFERENCES vacancies(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (tag_id) REFERENCES tags(id) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE vacancies_contracts (
    vacancy_id INTEGER,
    contract_id INTEGER,
    PRIMARY KEY (vacancy_id, contract_id),
    FOREIGN KEY (vacancy_id) REFERENCES vacancies(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (contract_id) REFERENCES contracts(id) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE vacancies_levels (
    vacancy_id INTEGER,
    level_id INTEGER,
    PRIMARY KEY (vacancy_id, level_id),
    FOREIGN KEY (vacancy_id) REFERENCES vacancies(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (level_id) REFERENCES levels(id) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE vacancies_work_formats (
    vacancy_id INTEGER,
    work_format_id INTEGER,
    PRIMARY KEY (vacancy_id, work_format_id),
    FOREIGN KEY (vacancy_id) REFERENCES vacancies(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (work_format_id) REFERENCES work_formats(id) ON DELETE CASCADE ON UPDATE CASCADE
);
