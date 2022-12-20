

CREATE TABLE "Container" (
	observation_list TEXT, 
	PRIMARY KEY (observation_list)
);

CREATE TABLE "Observation" (
	basin3d_id TEXT NOT NULL, 
	description TEXT, 
	categories TEXT, 
	units TEXT, 
	PRIMARY KEY (basin3d_id)
);
