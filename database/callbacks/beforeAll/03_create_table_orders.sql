-- Table: public.orders

-- DROP TABLE IF EXISTS public.orders;

CREATE TABLE IF NOT EXISTS public.orders
(
    order_id integer NOT NULL DEFAULT nextval('orders_order_id_seq'::regclass),
    name text COLLATE pg_catalog."default" NOT NULL,
    status text COLLATE pg_catalog."default" NOT NULL,
    user_id integer NOT NULL,
    crepe_id integer,
    created_at date,
    note character varying COLLATE pg_catalog."default",
    CONSTRAINT orders_pkey PRIMARY KEY (order_id),
    CONSTRAINT crepe_id FOREIGN KEY (crepe_id)
        REFERENCES public.crepes (crepe_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT user_id FOREIGN KEY (user_id)
        REFERENCES public.users (user_id) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE CASCADE
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.orders
    OWNER to postgres;
-- Index: fki_crepe_id

-- DROP INDEX IF EXISTS public.fki_crepe_id;

CREATE INDEX IF NOT EXISTS fki_crepe_id
    ON public.orders USING btree
    (crepe_id ASC NULLS LAST)
    TABLESPACE pg_default;
-- Index: fki_user

-- DROP INDEX IF EXISTS public.fki_user;

CREATE INDEX IF NOT EXISTS fki_user
    ON public.orders USING btree
    (user_id ASC NULLS LAST)
    TABLESPACE pg_default;