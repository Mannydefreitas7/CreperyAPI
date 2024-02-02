-- Table: public.toppings

-- DROP TABLE IF EXISTS public.toppings;

CREATE TABLE
IF NOT EXISTS public.toppings
(
    topping_id integer NOT NULL DEFAULT nextval
('toppings_topping_id_seq'::regclass),
    name character varying COLLATE pg_catalog."default" NOT NULL,
    calories character varying COLLATE pg_catalog."default",
    image_data bytea,
    crepe_id integer,
    CONSTRAINT toppings_pkey PRIMARY KEY
(topping_id)
)

TABLESPACE pg_default;

ALTER TABLE
IF EXISTS public.toppings
    OWNER to postgres;