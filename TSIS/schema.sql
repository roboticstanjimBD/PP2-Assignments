-- =========================================
-- Create Groups Table
-- =========================================

CREATE TABLE IF NOT EXISTS groups (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL
);

-- =========================================
-- Update Contacts Table
-- =========================================

ALTER TABLE contacts
ADD COLUMN IF NOT EXISTS email VARCHAR(100);

ALTER TABLE contacts
ADD COLUMN IF NOT EXISTS birthday DATE;

ALTER TABLE contacts
ADD COLUMN IF NOT EXISTS group_id INTEGER;

ALTER TABLE contacts
ADD CONSTRAINT fk_group
FOREIGN KEY (group_id)
REFERENCES groups(id);

-- =========================================
-- Create Phones Table
-- =========================================

CREATE TABLE IF NOT EXISTS phones (
    id SERIAL PRIMARY KEY,
    contact_id INTEGER REFERENCES contacts(id) ON DELETE CASCADE,
    phone VARCHAR(20) NOT NULL,
    type VARCHAR(10)
    CHECK (type IN ('home','work','mobile'))
);

INSERT INTO groups(name)
VALUES
('Family'),
('Friend'),
('Work'),
('Other')
ON CONFLICT (name) DO NOTHING;