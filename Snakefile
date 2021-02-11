configfile: "configs/configuser.yaml"


rule get_text:
	input:
		scripta="scripts/getarticle.py",	
	params:
		urlname=config["url-name"]
	output:
		article=config["pathout-txt"]
	conda:
		"envs/wordcloud.yaml"
	shell:
		"python {input.scripta} {params.urlname} {output.article}"

rule get_plot:
	input:
		scriptb="scripts/getplot.py"
	params:
		urlname=config["url-name"]
	output:
		pnga=config["pathout-png"]
	conda:
		"envs/wordcloud.yaml"
	shell:
		"python {input.scriptb} {params.urlname} {output.pnga} "

rule get_shape:
	input: 
		scriptc="scripts/getshape.py",
		pngb=config["pathin-shape"]
	params: 
		urlname=config["url-name"]
	output:
		pngc=config["pathout-shape"]
	conda:
		"envs/wordcloud.yaml"
	shell:
		"python {input.scriptc} {params.urlname} {input.pngb} {output.pngc}" 
