--
-- PostgreSQL database dump
--

-- Dumped from database version 11.1 (Debian 11.1-1.pgdg90+1)
-- Dumped by pg_dump version 11.1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: crdc; Type: SCHEMA; Schema: -; Owner: -
--

CREATE SCHEMA crdc;


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: lea_characteristics_table; Type: TABLE; Schema: crdc; Owner: -
--

CREATE TABLE crdc.lea_characteristics_table (
    leaid text NOT NULL,
    lea_enr bigint,
    lea_enr_nonleafac bigint,
    lea_schools bigint,
    lea_crcoord_sex_ind text,
    lea_crcoord_rac_ind text,
    lea_crcoord_dis_ind text,
    lea_crcoord_sex_fn text,
    lea_crcoord_sex_ln text,
    lea_crcoord_sex_ph text,
    lea_crcoord_sex_em text,
    lea_crcoord_rac_fn text,
    lea_crcoord_rac_ln text,
    lea_crcoord_rac_ph text,
    lea_crcoord_rac_em text,
    lea_crcoord_dis_fn text,
    lea_crcoord_dis_ln text,
    lea_crcoord_dis_ph text,
    lea_crcoord_dis_em text,
    lea_desegplan text,
    lea_hbpolicy_ind text,
    lea_hbpolicyurl_ind text,
    lea_hbpolicy_url text,
    lea_ece_ind text,
    lea_ece_nonidea text,
    lea_ps_ind text,
    lea_ps_fulldayfree text,
    lea_ps_fulldaycost text,
    lea_ps_partdayfree text,
    lea_ps_partdaycost text,
    lea_psenr_nonidea_a3 text,
    lea_psenr_nonidea_a4 text,
    lea_psenr_nonidea_a5 text,
    lea_psenr_a2 bigint,
    lea_psenr_a3 bigint,
    lea_psenr_a4 bigint,
    lea_psenr_a5 bigint,
    lea_pselig_all text,
    lea_pselig_idea text,
    lea_pselig_titlei text,
    lea_pselig_lowinc text,
    lea_kg_ind text,
    lea_kg_fulldayfree text,
    lea_kg_fulldaycost text,
    lea_kg_partdayfree text,
    lea_kg_partdaycost text
);


--
-- Name: lea_characteristics; Type: VIEW; Schema: crdc; Owner: -
--

CREATE VIEW crdc.lea_characteristics AS
 SELECT lea_characteristics_table.leaid,
    lea_characteristics_table.lea_enr AS enrollment,
    lea_characteristics_table.lea_enr_nonleafac AS enrollment_nonlea_facility,
    lea_characteristics_table.lea_schools AS schools,
    lea_characteristics_table.lea_crcoord_sex_ind AS coordinator_sex_indicator,
    lea_characteristics_table.lea_crcoord_rac_ind AS coordinator_race_indicator,
    lea_characteristics_table.lea_crcoord_dis_ind AS coordinator_disability_indicator,
    lea_characteristics_table.lea_crcoord_sex_fn AS coordinator_sex_first_name,
    lea_characteristics_table.lea_crcoord_sex_ln AS coordinator_sex_last_name,
    lea_characteristics_table.lea_crcoord_sex_ph AS coordinator_sex_phone,
    lea_characteristics_table.lea_crcoord_sex_em AS coordinator_sex_email,
    lea_characteristics_table.lea_crcoord_rac_fn AS coordinator_race_first_name,
    lea_characteristics_table.lea_crcoord_rac_ln AS coordinator_race_last_name,
    lea_characteristics_table.lea_crcoord_rac_ph AS coordinator_race_phone,
    lea_characteristics_table.lea_crcoord_rac_em AS coordinator_race_email,
    lea_characteristics_table.lea_crcoord_dis_fn AS coordinator_disability_first_name,
    lea_characteristics_table.lea_crcoord_dis_ln AS coordinator_disability_last_name,
    lea_characteristics_table.lea_crcoord_dis_ph AS coordinator_disability_phone,
    lea_characteristics_table.lea_crcoord_dis_em AS coordinator_disability_email,
    lea_characteristics_table.lea_desegplan AS desegregation_plan,
    lea_characteristics_table.lea_hbpolicy_ind AS harrassment_bullying_policy_indicator,
    lea_characteristics_table.lea_hbpolicyurl_ind AS harrassment_bullying_policy_url_indicator,
    lea_characteristics_table.lea_hbpolicy_url AS harrassment_bullying_policy_url,
    lea_characteristics_table.lea_ece_ind AS early_childhood_indicator,
    lea_characteristics_table.lea_ece_nonidea AS early_childhood_nonidea,
    lea_characteristics_table.lea_ps_ind AS preschool_indicator,
    lea_characteristics_table.lea_ps_fulldayfree AS preschool_fulldayfree,
    lea_characteristics_table.lea_ps_fulldaycost AS preschool_fulldaycost,
    lea_characteristics_table.lea_ps_partdayfree AS preschool_partdayfree,
    lea_characteristics_table.lea_ps_partdaycost AS preschool_partdaycost,
    lea_characteristics_table.lea_psenr_nonidea_a3 AS preschool_enrollment_nonidea_a3,
    lea_characteristics_table.lea_psenr_nonidea_a4 AS preschool_enrollment_nonidea_a4,
    lea_characteristics_table.lea_psenr_nonidea_a5 AS preschool_enrollment_nonidea_a5,
    lea_characteristics_table.lea_psenr_a2 AS preschool_enrollment_a2,
    lea_characteristics_table.lea_psenr_a3 AS preschool_enrollment_a3,
    lea_characteristics_table.lea_psenr_a4 AS preschool_enrollment_a4,
    lea_characteristics_table.lea_psenr_a5 AS preschool_enrollment_a5,
    lea_characteristics_table.lea_pselig_all AS preschool_eligibility_all,
    lea_characteristics_table.lea_pselig_idea AS preschool_eligibility_idea,
    lea_characteristics_table.lea_pselig_titlei AS preschool_eligibility_title_i,
    lea_characteristics_table.lea_pselig_lowinc AS preschool_eligibility_low_income,
    lea_characteristics_table.lea_kg_ind AS kindergarten_indicator,
    lea_characteristics_table.lea_kg_fulldayfree AS kindergarten_fulldayfree,
    lea_characteristics_table.lea_kg_fulldaycost AS kindergarten_fulldaycost,
    lea_characteristics_table.lea_kg_partdayfree AS kindergarten_partdayfree,
    lea_characteristics_table.lea_kg_partdaycost AS kindergarten_partdaycost
   FROM crdc.lea_characteristics_table;


--
-- Name: lea_distance_education_table; Type: TABLE; Schema: crdc; Owner: -
--

CREATE TABLE crdc.lea_distance_education_table (
    leaid text NOT NULL,
    lea_disted_ind text,
    lea_distedenr_hi_m bigint,
    lea_distedenr_hi_f bigint,
    lea_distedenr_am_m bigint,
    lea_distedenr_am_f bigint,
    lea_distedenr_as_m bigint,
    lea_distedenr_as_f bigint,
    lea_distedenr_hp_m bigint,
    lea_distedenr_hp_f bigint,
    lea_distedenr_bl_m bigint,
    lea_distedenr_bl_f bigint,
    lea_distedenr_wh_m bigint,
    lea_distedenr_wh_f bigint,
    lea_distedenr_tr_m bigint,
    lea_distedenr_tr_f bigint,
    tot_distedenr_m bigint,
    tot_distedenr_f bigint,
    lea_distedenr_lep_m bigint,
    lea_distedenr_lep_f bigint,
    lea_distedenr_idea_m bigint,
    lea_distedenr_idea_f bigint
);


--
-- Name: lea_distance_education; Type: VIEW; Schema: crdc; Owner: -
--

CREATE VIEW crdc.lea_distance_education AS
 SELECT lea_distance_education_table.leaid,
    lea_distance_education_table.lea_disted_ind AS indicator,
    lea_distance_education_table.lea_distedenr_hi_m AS enrollment_hispanic_male,
    lea_distance_education_table.lea_distedenr_hi_f AS enrollment_hispanic_female,
    lea_distance_education_table.lea_distedenr_am_m AS enrollment_american_indian_male,
    lea_distance_education_table.lea_distedenr_am_f AS enrollment_american_indian_female,
    lea_distance_education_table.lea_distedenr_as_m AS enrollment_asian_male,
    lea_distance_education_table.lea_distedenr_as_f AS enrollment_asian_female,
    lea_distance_education_table.lea_distedenr_hp_m AS enrollment_pacific_islander_male,
    lea_distance_education_table.lea_distedenr_hp_f AS enrollment_pacific_islander_female,
    lea_distance_education_table.lea_distedenr_bl_m AS enrollment_black_male,
    lea_distance_education_table.lea_distedenr_bl_f AS enrollment_black_female,
    lea_distance_education_table.lea_distedenr_wh_m AS enrollment_white_male,
    lea_distance_education_table.lea_distedenr_wh_f AS enrollment_white_female,
    lea_distance_education_table.lea_distedenr_tr_m AS enrollment_multiracial_male,
    lea_distance_education_table.lea_distedenr_tr_f AS enrollment_multiracial_female,
    lea_distance_education_table.tot_distedenr_m AS total_enrollment_male,
    lea_distance_education_table.tot_distedenr_f AS total_enrollment_female,
    lea_distance_education_table.lea_distedenr_lep_m AS enrollment_lep_male,
    lea_distance_education_table.lea_distedenr_lep_f AS enrollment_lep_female,
    lea_distance_education_table.lea_distedenr_idea_m AS enrollment_idea_male,
    lea_distance_education_table.lea_distedenr_idea_f AS enrollment_idea_female
   FROM crdc.lea_distance_education_table;


--
-- Name: lea_high_school_equivalency_(ged)_table; Type: TABLE; Schema: crdc; Owner: -
--

CREATE TABLE crdc."lea_high_school_equivalency_(ged)_table" (
    leaid text NOT NULL,
    lea_ged_ind text,
    lea_gedpart_hi_m bigint,
    lea_gedpart_hi_f bigint,
    lea_gedpart_am_m bigint,
    lea_gedpart_am_f bigint,
    lea_gedpart_as_m bigint,
    lea_gedpart_as_f bigint,
    lea_gedpart_hp_m bigint,
    lea_gedpart_hp_f bigint,
    lea_gedpart_bl_m bigint,
    lea_gedpart_bl_f bigint,
    lea_gedpart_wh_m bigint,
    lea_gedpart_wh_f bigint,
    lea_gedpart_tr_m bigint,
    lea_gedpart_tr_f bigint,
    tot_gedpart_m bigint,
    tot_gedpart_f bigint,
    lea_gedpart_lep_m bigint,
    lea_gedpart_lep_f bigint,
    lea_gedpart_idea_m bigint,
    lea_gedpart_idea_f bigint,
    lea_gedcred_hi_m bigint,
    lea_gedcred_hi_f bigint,
    lea_gedcred_am_m bigint,
    lea_gedcred_am_f bigint,
    lea_gedcred_as_m bigint,
    lea_gedcred_as_f bigint,
    lea_gedcred_hp_m bigint,
    lea_gedcred_hp_f bigint,
    lea_gedcred_bl_m bigint,
    lea_gedcred_bl_f bigint,
    lea_gedcred_wh_m bigint,
    lea_gedcred_wh_f bigint,
    lea_gedcred_tr_m bigint,
    lea_gedcred_tr_f bigint,
    tot_gedcred_m bigint,
    tot_gedcred_f bigint,
    lea_gedcred_lep_m bigint,
    lea_gedcred_lep_f bigint,
    lea_gedcred_idea_m bigint,
    lea_gedcred_idea_f bigint
);


--
-- Name: lea_high_school_equivalency_(ged); Type: VIEW; Schema: crdc; Owner: -
--

CREATE VIEW crdc."lea_high_school_equivalency_(ged)" AS
 SELECT "lea_high_school_equivalency_(ged)_table".leaid,
    "lea_high_school_equivalency_(ged)_table".lea_ged_ind AS indicator,
    "lea_high_school_equivalency_(ged)_table".lea_gedpart_hi_m AS participants_hispanic_male,
    "lea_high_school_equivalency_(ged)_table".lea_gedpart_hi_f AS participants_hispanic_female,
    "lea_high_school_equivalency_(ged)_table".lea_gedpart_am_m AS participants_american_indian_male,
    "lea_high_school_equivalency_(ged)_table".lea_gedpart_am_f AS participants_american_indian_female,
    "lea_high_school_equivalency_(ged)_table".lea_gedpart_as_m AS participants_asian_male,
    "lea_high_school_equivalency_(ged)_table".lea_gedpart_as_f AS participants_asian_female,
    "lea_high_school_equivalency_(ged)_table".lea_gedpart_hp_m AS participants_pacific_islander_male,
    "lea_high_school_equivalency_(ged)_table".lea_gedpart_hp_f AS participants_pacific_islander_female,
    "lea_high_school_equivalency_(ged)_table".lea_gedpart_bl_m AS participants_black_male,
    "lea_high_school_equivalency_(ged)_table".lea_gedpart_bl_f AS participants_black_female,
    "lea_high_school_equivalency_(ged)_table".lea_gedpart_wh_m AS participants_white_male,
    "lea_high_school_equivalency_(ged)_table".lea_gedpart_wh_f AS participants_white_female,
    "lea_high_school_equivalency_(ged)_table".lea_gedpart_tr_m AS participants_multiracial_male,
    "lea_high_school_equivalency_(ged)_table".lea_gedpart_tr_f AS participants_multiracial_female,
    "lea_high_school_equivalency_(ged)_table".tot_gedpart_m AS total_participants_male,
    "lea_high_school_equivalency_(ged)_table".tot_gedpart_f AS total_participants_female,
    "lea_high_school_equivalency_(ged)_table".lea_gedpart_lep_m AS participants_lep_male,
    "lea_high_school_equivalency_(ged)_table".lea_gedpart_lep_f AS participants_lep_female,
    "lea_high_school_equivalency_(ged)_table".lea_gedpart_idea_m AS participants_idea_male,
    "lea_high_school_equivalency_(ged)_table".lea_gedpart_idea_f AS participants_idea_female,
    "lea_high_school_equivalency_(ged)_table".lea_gedcred_hi_m AS credential_hispanic_male,
    "lea_high_school_equivalency_(ged)_table".lea_gedcred_hi_f AS credential_hispanic_female,
    "lea_high_school_equivalency_(ged)_table".lea_gedcred_am_m AS credential_american_indian_male,
    "lea_high_school_equivalency_(ged)_table".lea_gedcred_am_f AS credential_american_indian_female,
    "lea_high_school_equivalency_(ged)_table".lea_gedcred_as_m AS credential_asian_male,
    "lea_high_school_equivalency_(ged)_table".lea_gedcred_as_f AS credential_asian_female,
    "lea_high_school_equivalency_(ged)_table".lea_gedcred_hp_m AS credential_pacific_islander_male,
    "lea_high_school_equivalency_(ged)_table".lea_gedcred_hp_f AS credential_pacific_islander_female,
    "lea_high_school_equivalency_(ged)_table".lea_gedcred_bl_m AS credential_black_male,
    "lea_high_school_equivalency_(ged)_table".lea_gedcred_bl_f AS credential_black_female,
    "lea_high_school_equivalency_(ged)_table".lea_gedcred_wh_m AS credential_white_male,
    "lea_high_school_equivalency_(ged)_table".lea_gedcred_wh_f AS credential_white_female,
    "lea_high_school_equivalency_(ged)_table".lea_gedcred_tr_m AS credential_multiracial_male,
    "lea_high_school_equivalency_(ged)_table".lea_gedcred_tr_f AS credential_multiracial_female,
    "lea_high_school_equivalency_(ged)_table".tot_gedcred_m AS total_credential_male,
    "lea_high_school_equivalency_(ged)_table".tot_gedcred_f AS total_credential_female,
    "lea_high_school_equivalency_(ged)_table".lea_gedcred_lep_m AS credential_lep_male,
    "lea_high_school_equivalency_(ged)_table".lea_gedcred_lep_f AS credential_lep_female,
    "lea_high_school_equivalency_(ged)_table".lea_gedcred_idea_m AS credential_idea_male,
    "lea_high_school_equivalency_(ged)_table".lea_gedcred_idea_f AS credential_idea_female
   FROM crdc."lea_high_school_equivalency_(ged)_table";


--
-- Name: lea_identification_table; Type: TABLE; Schema: crdc; Owner: -
--

CREATE TABLE crdc.lea_identification_table (
    leaid text NOT NULL,
    lea_state text,
    lea_state_name text,
    lea_name text,
    lea_address text,
    lea_city text,
    lea_zip text,
    cjj text
);


--
-- Name: lea_identification; Type: VIEW; Schema: crdc; Owner: -
--

CREATE VIEW crdc.lea_identification AS
 SELECT lea_identification_table.leaid,
    lea_identification_table.lea_state AS state,
    lea_identification_table.lea_state_name AS state_name,
    lea_identification_table.lea_name AS name,
    lea_identification_table.lea_address AS address,
    lea_identification_table.lea_city AS city,
    lea_identification_table.lea_zip AS zip,
    lea_identification_table.cjj AS contains_jj_facility
   FROM crdc.lea_identification_table;


--
-- Name: lea_characteristics_table lea_characteristics_table_pkey; Type: CONSTRAINT; Schema: crdc; Owner: -
--

ALTER TABLE ONLY crdc.lea_characteristics_table
    ADD CONSTRAINT lea_characteristics_table_pkey PRIMARY KEY (leaid);


--
-- Name: lea_distance_education_table lea_distance_education_table_pkey; Type: CONSTRAINT; Schema: crdc; Owner: -
--

ALTER TABLE ONLY crdc.lea_distance_education_table
    ADD CONSTRAINT lea_distance_education_table_pkey PRIMARY KEY (leaid);


--
-- Name: lea_high_school_equivalency_(ged)_table lea_high_school_equivalency_(ged)_table_pkey; Type: CONSTRAINT; Schema: crdc; Owner: -
--

ALTER TABLE ONLY crdc."lea_high_school_equivalency_(ged)_table"
    ADD CONSTRAINT "lea_high_school_equivalency_(ged)_table_pkey" PRIMARY KEY (leaid);


--
-- Name: lea_identification_table lea_identification_table_pkey; Type: CONSTRAINT; Schema: crdc; Owner: -
--

ALTER TABLE ONLY crdc.lea_identification_table
    ADD CONSTRAINT lea_identification_table_pkey PRIMARY KEY (leaid);


--
-- Name: ix_crdc_lea_characteristics_table_leaid; Type: INDEX; Schema: crdc; Owner: -
--

CREATE INDEX ix_crdc_lea_characteristics_table_leaid ON crdc.lea_characteristics_table USING btree (leaid);


--
-- Name: ix_crdc_lea_distance_education_table_leaid; Type: INDEX; Schema: crdc; Owner: -
--

CREATE INDEX ix_crdc_lea_distance_education_table_leaid ON crdc.lea_distance_education_table USING btree (leaid);


--
-- Name: ix_crdc_lea_high_school_equivalency_(ged)_table_leaid; Type: INDEX; Schema: crdc; Owner: -
--

CREATE INDEX "ix_crdc_lea_high_school_equivalency_(ged)_table_leaid" ON crdc."lea_high_school_equivalency_(ged)_table" USING btree (leaid);


--
-- Name: ix_crdc_lea_identification_table_leaid; Type: INDEX; Schema: crdc; Owner: -
--

CREATE INDEX ix_crdc_lea_identification_table_leaid ON crdc.lea_identification_table USING btree (leaid);


--
-- PostgreSQL database dump complete
--

