CREATE TABLE IF NOT EXISTS public.crepes
(
    crepe_id integer NOT NULL,
    name text COLLATE pg_catalog."default" NOT NULL,
    image_data bytea NOT NULL,
    order_id integer,
    topping_id integer,
    created_at date,
    description character varying COLLATE pg_catalog."default",
    CONSTRAINT crepes_pkey PRIMARY KEY (crepe_id),
    CONSTRAINT order_id FOREIGN KEY (order_id)
        REFERENCES public.orders (order_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT topping_id FOREIGN KEY (topping_id)
        REFERENCES public.toppings (topping_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
);


ALTER TABLE IF EXISTS public.crepes
    OWNER to postgres;

CREATE INDEX IF NOT EXISTS fki_order_id
    ON public.crepes USING btree
    (order_id ASC NULLS LAST);

CREATE INDEX IF NOT EXISTS fki_topping_id
    ON public.crepes USING btree
    (topping_id ASC NULLS LAST);