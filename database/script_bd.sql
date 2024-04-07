
BEGIN;


CREATE TABLE IF NOT EXISTS public.tb_aproved
(
    id serial NOT NULL,
    id_employee integer NOT NULL,
    id_report_filtration integer NOT NULL,
    CONSTRAINT tb_aproved_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.tb_assets_tc
(
    id serial NOT NULL,
    as_name character varying COLLATE pg_catalog."default",
    as_description character varying COLLATE pg_catalog."default",
    as_quantity character varying COLLATE pg_catalog."default",
    CONSTRAINT tb_assets_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.tb_cicles_ft
(
    id serial NOT NULL,
    ft_num_cicles character varying COLLATE pg_catalog."default",
    CONSTRAINT tb_cicles_ft_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.tb_competency_profiles_tc
(
    id serial NOT NULL,
    cp_name character varying(50) COLLATE pg_catalog."default",
    cp_unit_completed character varying(50) COLLATE pg_catalog."default",
    cp_element_completed character varying(50) COLLATE pg_catalog."default",
    cp_perc_completed_date character varying(50) COLLATE pg_catalog."default",
    cp_comment character varying(50) COLLATE pg_catalog."default",
    id_physical_person integer,
    id_report_tc integer,
    CONSTRAINT tb_competency_profiles_tc_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.tb_consumables_tc
(
    id serial NOT NULL,
    cs_name character varying COLLATE pg_catalog."default",
    cs_description character varying COLLATE pg_catalog."default",
    cs_quantity character varying COLLATE pg_catalog."default",
    CONSTRAINT tb_consumables_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.tb_consumiveis
(
    id serial NOT NULL,
    nome_consumivel character varying COLLATE pg_catalog."default",
    initial_stock integer,
    CONSTRAINT tb_consumiveis_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.tb_daily_progress_tc
(
    id serial NOT NULL,
    dp_description character varying(500) COLLATE pg_catalog."default",
    id_physical_person integer,
    CONSTRAINT tb_daily_progress_tc_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.tb_employee_cp
(
    id serial NOT NULL,
    emp_name character varying COLLATE pg_catalog."default",
    emp_email character varying COLLATE pg_catalog."default",
    CONSTRAINT tb_employee_compliance_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.tb_employee_ft
(
    id serial NOT NULL,
    emp_name character varying COLLATE pg_catalog."default",
    emp_email character varying COLLATE pg_catalog."default",
    CONSTRAINT tb_employee_filtration_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.tb_employee_tc
(
    id serial NOT NULL,
    emp_name character varying COLLATE pg_catalog."default",
    emp_email character varying COLLATE pg_catalog."default",
    CONSTRAINT tb_employee_tank_cleaning_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.tb_employee_wbco
(
    id serial NOT NULL,
    emp_name character varying COLLATE pg_catalog."default",
    emp_email character varying COLLATE pg_catalog."default",
    emp_personal_position integer,
    CONSTRAINT tb_employee_wbco_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.tb_engineer_ft
(
    id_engineer serial NOT NULL,
    eng_shift character varying COLLATE pg_catalog."default",
    eng_total_dayst character varying COLLATE pg_catalog."default",
    id_employee integer,
    id_report_ft integer,
    CONSTRAINT tb_engineer_ft_pkey PRIMARY KEY (id_engineer)
);

CREATE TABLE IF NOT EXISTS public.tb_engineer_tc
(
    id serial NOT NULL,
    tc_eng_shift character varying(50) COLLATE pg_catalog."default",
    tc_eng_total_dayst character varying(50) COLLATE pg_catalog."default",
    id_physical_person integer,
    id_report_tc integer,
    CONSTRAINT tb_enginier_tc_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.tb_engineer_wbco
(
    id serial NOT NULL,
    wb_eng_shift character varying(50) COLLATE pg_catalog."default",
    wb_eng_total_dayst character varying(50) COLLATE pg_catalog."default",
    id_employee integer,
    id_report_wbco integer,
    CONSTRAINT tb_engineer_wbco_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.tb_filtration_consumables_ft
(
    id integer NOT NULL,
    id_type integer,
    ft_openning_stock integer,
    ft_additional_stock integer,
    ft_total_stock integer,
    ft_daily_used integer,
    ft_total_used integer,
    ft_closing_bal integer,
    id_report_ft integer,
    id_consumivel integer NOT NULL,
    CONSTRAINT tb_filtration_cons_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.tb_fluid_analisys_ft
(
    id serial NOT NULL,
    ft_wellbone_displacement character varying(50) COLLATE pg_catalog."default",
    ft_time character varying(50) COLLATE pg_catalog."default",
    ft_pumping_time character varying(50) COLLATE pg_catalog."default",
    ft_volume_pumped character varying(50) COLLATE pg_catalog."default",
    ft_ntu character varying(50) COLLATE pg_catalog."default",
    ft_tss_perc_solids character varying(50) COLLATE pg_catalog."default",
    ft_sample character varying(50) COLLATE pg_catalog."default",
    id_report_ft integer,
    CONSTRAINT tb_fluid_analisys_ft_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.tb_fluid_consumables_ft
(
    id serial NOT NULL,
    ft_type integer,
    ft_time character varying(50) COLLATE pg_catalog."default",
    ft_openning_stock double precision,
    ft_additional_stock double precision,
    ft_total_stock double precision,
    ft_daily_used double precision,
    ft_total_used double precision,
    ft_closing_bal double precision,
    id_physical_person integer,
    id_report_ft integer,
    CONSTRAINT tb_fluid_consumables_ft_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.tb_fluid_consumables_type_ft
(
    id serial NOT NULL,
    description character varying(50) COLLATE pg_catalog."default",
    CONSTRAINT tb_fluid_consumables_type_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.tb_fluid_information_ft
(
    id serial NOT NULL,
    ft_fluid_type_filtered character varying(50) COLLATE pg_catalog."default",
    ft_daily_total integer,
    ft_density_sg double precision,
    ft_density_type character varying(50) COLLATE pg_catalog."default",
    ft_viscosity character varying(50) COLLATE pg_catalog."default",
    ft_hole_volume character varying(50) COLLATE pg_catalog."default",
    ft_hole_volume_type character varying(50) COLLATE pg_catalog."default",
    ft_vol_filtered_date character varying(50) COLLATE pg_catalog."default",
    id_report_ft integer,
    CONSTRAINT tb_fluid_information_ft_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.tb_fluid_sumary_ft
(
    id serial NOT NULL,
    ft_start_time character varying(50) COLLATE pg_catalog."default",
    ft_stop_time character varying(60) COLLATE pg_catalog."default",
    ft_total_minutes_per_cicles integer,
    ft_volume_per_cicles double precision,
    ft_volume_per_cicles_type character varying(50) COLLATE pg_catalog."default",
    ft_d_e_per_cicle_20kg double precision,
    ft_cartridge_filtrers integer,
    id_report_ft integer,
    id_num_cicle integer,
    CONSTRAINT tb_fluid_sumary_ft_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.tb_hole_volume_type
(
    id integer NOT NULL,
    description character varying COLLATE pg_catalog."default",
    CONSTRAINT tb_hole_volume_type_wbco_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.tb_hse_tc
(
    id serial NOT NULL,
    hse_quantity integer,
    hse_comments character varying(100) COLLATE pg_catalog."default",
    id_typehse integer,
    id_report_tc integer,
    CONSTRAINT tb_hse_tc_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.tb_legal_person
(
    id serial NOT NULL,
    lp_nif character varying(50) COLLATE pg_catalog."default" NOT NULL,
    lp_name character varying(50) COLLATE pg_catalog."default" NOT NULL,
    lp_email character varying(50) COLLATE pg_catalog."default" NOT NULL,
    lp_phone character varying(50) COLLATE pg_catalog."default" NOT NULL,
    lp_logo character varying(50) COLLATE pg_catalog."default" NOT NULL,
    lp_address character varying(50) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT tb_legal_person_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.tb_non_produtive_man_tc
(
    id serial NOT NULL,
    npm_hours character varying(50) COLLATE pg_catalog."default",
    npm_comments character varying(50) COLLATE pg_catalog."default",
    id_non_produtive_type integer,
    id_report_tc integer,
    CONSTRAINT tb_non_prod_man_tc_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.tb_non_produtive_type_tc
(
    id serial NOT NULL,
    npt_description character varying(50) COLLATE pg_catalog."default",
    CONSTRAINT tb_non_prod_tc_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.tb_period_tc
(
    id serial NOT NULL,
    pr_type character varying(10) COLLATE pg_catalog."default",
    CONSTRAINT tb_period_tc_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.tb_personal_position
(
    id serial NOT NULL,
    pp_description character varying COLLATE pg_catalog."default",
    CONSTRAINT tb_personal_position_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.tb_physical_person
(
    id serial NOT NULL,
    bi character varying(50) COLLATE pg_catalog."default" NOT NULL,
    pp_name character varying(50) COLLATE pg_catalog."default" NOT NULL,
    pp_email character varying(50) COLLATE pg_catalog."default" NOT NULL,
    pp_senha character varying(50) COLLATE pg_catalog."default" NOT NULL,
    pp_phone character varying(50) COLLATE pg_catalog."default" NOT NULL,
    pp_type character varying(50) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT tb_physical_person_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.tb_pipe_tc
(
    id serial NOT NULL,
    pi_name character varying COLLATE pg_catalog."default",
    pi_description character varying COLLATE pg_catalog."default",
    pi_quantity character varying COLLATE pg_catalog."default",
    CONSTRAINT tb_pipe_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.tb_prepared
(
    id serial NOT NULL,
    id_report_filtration integer NOT NULL,
    id_physical_person integer,
    CONSTRAINT tb_prepared_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.tb_produtive_man_tc
(
    id serial NOT NULL,
    pm_work_order character varying(50) COLLATE pg_catalog."default",
    pm_description character varying(50) COLLATE pg_catalog."default",
    pm_original_hours character varying(50) COLLATE pg_catalog."default",
    pm_hours_brocked_td character varying(50) COLLATE pg_catalog."default",
    pm_qt_hours_brocked_td character varying(50) COLLATE pg_catalog."default",
    pm_hours_brocked_date character varying(50) COLLATE pg_catalog."default",
    pm_hours_remaining_td character varying(50) COLLATE pg_catalog."default",
    pm_visual_perc_complete character varying(50) COLLATE pg_catalog."default",
    id_report_tc integer,
    CONSTRAINT tb_produtive_tc_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.tb_project_description_tc
(
    id serial NOT NULL,
    pd_description character varying(100) COLLATE pg_catalog."default",
    id_physical_person integer,
    CONSTRAINT tb_project_description_tc_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.tb_report_ft
(
    id serial NOT NULL,
    ft_ongoing_rig_activity character varying(500) COLLATE pg_catalog."default",
    ft_filtration_activity character varying(500) COLLATE pg_catalog."default",
    id_legal_person integer,
    id_report_header integer,
    CONSTRAINT tb_report_ft_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.tb_report_header
(
    id serial NOT NULL,
    rpt_job_ref_number character varying(50) COLLATE pg_catalog."default",
    rpt_field_locations character varying(50) COLLATE pg_catalog."default",
    rpt_job_type character varying(50) COLLATE pg_catalog."default",
    rpt_shift character varying(50) COLLATE pg_catalog."default",
    rpt_report_date character varying(50) COLLATE pg_catalog."default",
    id_physical_person integer,
    rpt_rig_name character varying COLLATE pg_catalog."default",
    CONSTRAINT tb_report_header_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.tb_report_tc
(
    id serial NOT NULL,
    id_physical_person integer,
    id_legal_person integer,
    id_shit_activity_tc integer,
    id_employee integer,
    id_report_header integer,
    CONSTRAINT tb_report_tc_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.tb_report_wbco
(
    id serial NOT NULL,
    rpt_ongoing_rig character varying(100) COLLATE pg_catalog."default",
    rpt_casing_size integer,
    rpt_length character varying(50) COLLATE pg_catalog."default",
    rpt_od integer,
    rpt_id character varying(50) COLLATE pg_catalog."default",
    rpt_size character varying(50) COLLATE pg_catalog."default",
    rpt_weight_rangeng character varying(50) COLLATE pg_catalog."default",
    rpt_volume_capacity character varying(50) COLLATE pg_catalog."default",
    rpt_hole_volume character varying(50) COLLATE pg_catalog."default",
    rpt_wbco_tools_activity character varying(300) COLLATE pg_catalog."default",
    rpt_shift_supervisor character varying(50) COLLATE pg_catalog."default",
    rpt_total_day_supervisor integer,
    id_well integer,
    id_physical_person integer,
    id_legal_person integer,
    id_employee integer,
    id_report_header integer,
    CONSTRAINT tb_report_wbco_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.tb_shift_activity_tc
(
    id serial NOT NULL,
    pd_description character varying COLLATE pg_catalog."default",
    id_physical_person integer,
    daily_progress character varying COLLATE pg_catalog."default",
    planned_activity character varying COLLATE pg_catalog."default",
    norm_reading character varying COLLATE pg_catalog."default",
    equipament_material character varying COLLATE pg_catalog."default",
    CONSTRAINT tb_shift_activit_tc_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.tb_shift_tc
(
    id serial NOT NULL,
    sh_trade character varying(50) COLLATE pg_catalog."default",
    sh_planed_demmed character varying(50) COLLATE pg_catalog."default",
    sh_crew_change character varying(50) COLLATE pg_catalog."default",
    id_period integer,
    id_employee integer,
    id_report_tc integer,
    CONSTRAINT tb_shift_tc_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.tb_tank_information_tc
(
    id serial NOT NULL,
    ti_number_tank character varying COLLATE pg_catalog."default",
    ti_volume_waste character varying COLLATE pg_catalog."default",
    ti_type_waste character varying COLLATE pg_catalog."default",
    ti_tank_type character varying COLLATE pg_catalog."default",
    id_report_tc integer,
    CONSTRAINT tb_tank_information_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.tb_thread_con
(
    id serial NOT NULL,
    thc character varying COLLATE pg_catalog."default",
    thc_description character varying COLLATE pg_catalog."default",
    CONSTRAINT tb_thread_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.tb_tools_on_board_backup
(
    id serial NOT NULL,
    tlb_description character varying(50) COLLATE pg_catalog."default",
    tlb_size character varying(50) COLLATE pg_catalog."default",
    tlb_thead_connetions integer,
    tlb_od character varying(50) COLLATE pg_catalog."default",
    tlb_id character varying(50) COLLATE pg_catalog."default",
    tlb_drift_size character varying(50) COLLATE pg_catalog."default",
    id_physical_person integer,
    id_report_tools integer,
    CONSTRAINT tb_tools_on_board_backup_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.tb_tools_on_board_primary
(
    id serial NOT NULL,
    tl_description character varying(50) COLLATE pg_catalog."default",
    tl_size character varying(50) COLLATE pg_catalog."default",
    tl_thead_connetions integer,
    tl_od character varying(50) COLLATE pg_catalog."default",
    tl_id character varying(50) COLLATE pg_catalog."default",
    tl_drift_size character varying(50) COLLATE pg_catalog."default",
    id_physical_person integer,
    id_report_tools integer,
    CONSTRAINT tb_tools_on_board_primary_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.tb_typehse_tc
(
    id serial NOT NULL,
    thse_description character varying(50) COLLATE pg_catalog."default",
    CONSTRAINT tb_typehse_tc_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.tb_wbco_size
(
    id serial NOT NULL,
    size character varying COLLATE pg_catalog."default",
    description character varying COLLATE pg_catalog."default",
    CONSTRAINT tb_wbco_size_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.tb_well
(
    id serial NOT NULL,
    wl_number character varying(50) COLLATE pg_catalog."default",
    wl_name character varying(50) COLLATE pg_catalog."default",
    id_legal_person integer,
    id_physical_person integer,
    CONSTRAINT tb_well_pkey PRIMARY KEY (id)
);

ALTER TABLE IF EXISTS public.tb_aproved
    ADD CONSTRAINT tb_aproved_id_employee_fkey FOREIGN KEY (id_employee)
    REFERENCES public.tb_employee_ft (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE CASCADE;


ALTER TABLE IF EXISTS public.tb_aproved
    ADD CONSTRAINT tb_aproved_id_report_filtration_fkey FOREIGN KEY (id_report_filtration)
    REFERENCES public.tb_report_ft (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE CASCADE;


ALTER TABLE IF EXISTS public.tb_employee_wbco
    ADD CONSTRAINT tb_employee_wbco_emp_personal_position_fkey FOREIGN KEY (emp_personal_position)
    REFERENCES public.tb_personal_position (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE CASCADE;


ALTER TABLE IF EXISTS public.tb_engineer_ft
    ADD CONSTRAINT tb_engineer_ft_id_employee_fkey FOREIGN KEY (id_employee)
    REFERENCES public.tb_employee_ft (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE CASCADE;


ALTER TABLE IF EXISTS public.tb_engineer_ft
    ADD CONSTRAINT tb_engineer_ft_id_employee_fkey1 FOREIGN KEY (id_employee)
    REFERENCES public.tb_employee_ft (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE CASCADE;


ALTER TABLE IF EXISTS public.tb_filtration_consumables_ft
    ADD CONSTRAINT tb_filtration_consumables_ft_id_consumivel_fkey FOREIGN KEY (id_consumivel)
    REFERENCES public.tb_consumiveis (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE CASCADE;


ALTER TABLE IF EXISTS public.tb_filtration_consumables_ft
    ADD CONSTRAINT tb_filtration_consumables_ft_id_consumivel_fkey1 FOREIGN KEY (id_consumivel)
    REFERENCES public.tb_consumiveis (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE CASCADE;


ALTER TABLE IF EXISTS public.tb_filtration_consumables_ft
    ADD CONSTRAINT tb_filtration_consumables_ft_id_type_fkey FOREIGN KEY (id_type)
    REFERENCES public.tb_fluid_consumables_type_ft (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE CASCADE;


ALTER TABLE IF EXISTS public.tb_filtration_consumables_ft
    ADD CONSTRAINT tb_filtration_consumables_ft_id_type_fkey1 FOREIGN KEY (id_type)
    REFERENCES public.tb_fluid_consumables_type_ft (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE CASCADE;


ALTER TABLE IF EXISTS public.tb_fluid_analisys_ft
    ADD CONSTRAINT tb_fluid_analisys_ft_id_report_ft_fkey FOREIGN KEY (id_report_ft)
    REFERENCES public.tb_report_ft (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE CASCADE;


ALTER TABLE IF EXISTS public.tb_fluid_analisys_ft
    ADD CONSTRAINT tb_fluid_analisys_ft_id_report_ft_fkey1 FOREIGN KEY (id_report_ft)
    REFERENCES public.tb_report_ft (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE CASCADE;


ALTER TABLE IF EXISTS public.tb_prepared
    ADD CONSTRAINT tb_prepared_fkey FOREIGN KEY (id_physical_person)
    REFERENCES public.tb_physical_person (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE CASCADE;


ALTER TABLE IF EXISTS public.tb_prepared
    ADD CONSTRAINT tb_prepared_id_report__fkey FOREIGN KEY (id_report_filtration)
    REFERENCES public.tb_prepared (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE CASCADE;


ALTER TABLE IF EXISTS public.tb_report_wbco
    ADD CONSTRAINT tb_report_wbco_id_employee_fkey FOREIGN KEY (id_employee)
    REFERENCES public.tb_employee_wbco (id) MATCH SIMPLE
    ON UPDATE CASCADE
    ON DELETE CASCADE;


ALTER TABLE IF EXISTS public.tb_report_wbco
    ADD CONSTRAINT tb_report_wbco_id_legal_person_fkey FOREIGN KEY (id_legal_person)
    REFERENCES public.tb_legal_person (id) MATCH SIMPLE
    ON UPDATE CASCADE
    ON DELETE CASCADE;


ALTER TABLE IF EXISTS public.tb_report_wbco
    ADD CONSTRAINT tb_report_wbco_id_physical_person_fkey FOREIGN KEY (id_physical_person)
    REFERENCES public.tb_physical_person (id) MATCH SIMPLE
    ON UPDATE CASCADE
    ON DELETE CASCADE;


ALTER TABLE IF EXISTS public.tb_report_wbco
    ADD CONSTRAINT tb_report_wbco_id_report_header_fkey FOREIGN KEY (id_report_header)
    REFERENCES public.tb_report_header (id) MATCH SIMPLE
    ON UPDATE CASCADE
    ON DELETE CASCADE;


ALTER TABLE IF EXISTS public.tb_report_wbco
    ADD CONSTRAINT tb_report_wbco_id_well_fkey FOREIGN KEY (id_well)
    REFERENCES public.tb_well (id) MATCH SIMPLE
    ON UPDATE CASCADE
    ON DELETE CASCADE;


ALTER TABLE IF EXISTS public.tb_report_wbco
    ADD CONSTRAINT tb_report_wbco_rpt_casing_size_fkey FOREIGN KEY (rpt_casing_size)
    REFERENCES public.tb_wbco_size (id) MATCH SIMPLE
    ON UPDATE CASCADE
    ON DELETE CASCADE
    NOT VALID;


ALTER TABLE IF EXISTS public.tb_report_wbco
    ADD CONSTRAINT tb_report_wbco_rpt_od_fkey FOREIGN KEY (rpt_od)
    REFERENCES public.tb_wbco_size (id) MATCH SIMPLE
    ON UPDATE CASCADE
    ON DELETE CASCADE
    NOT VALID;


ALTER TABLE IF EXISTS public.tb_tank_information_tc
    ADD CONSTRAINT tb_tank_information_id_report__fkey FOREIGN KEY (id_report_tc)
    REFERENCES public.tb_report_tc (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE CASCADE;


ALTER TABLE IF EXISTS public.tb_tools_on_board_backup
    ADD CONSTRAINT tb_tools_on_board_backup_tlb_thead_connetions_fkey FOREIGN KEY (tlb_thead_connetions)
    REFERENCES public.tb_thread_con (id) MATCH SIMPLE
    ON UPDATE CASCADE
    ON DELETE CASCADE
    NOT VALID;


ALTER TABLE IF EXISTS public.tb_tools_on_board_primary
    ADD CONSTRAINT tb_tools_on_board_primary_tl_thead_connetions_fkey FOREIGN KEY (tl_thead_connetions)
    REFERENCES public.tb_thread_con (id) MATCH SIMPLE
    ON UPDATE CASCADE
    ON DELETE CASCADE
    NOT VALID;

END;