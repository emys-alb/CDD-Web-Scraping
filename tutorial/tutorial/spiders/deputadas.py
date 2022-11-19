import scrapy

content = ["https://www.camara.leg.br/deputados/204528",
            "https://www.camara.leg.br/deputados/204545",
            "https://www.camara.leg.br/deputados/74057",
            "https://www.camara.leg.br/deputados/204353",
            "https://www.camara.leg.br/deputados/204400",
            "https://www.camara.leg.br/deputados/73696",
            "https://www.camara.leg.br/deputados/123756",
            "https://www.camara.leg.br/deputados/204509",
            "https://www.camara.leg.br/deputados/73701",
            "https://www.camara.leg.br/deputados/204374",
            "https://www.camara.leg.br/deputados/160589",
            "https://www.camara.leg.br/deputados/213762",
            "https://www.camara.leg.br/deputados/204507",
            "https://www.camara.leg.br/deputados/164360",
            "https://www.camara.leg.br/deputados/204369",
            "https://www.camara.leg.br/deputados/204380",
            "https://www.camara.leg.br/deputados/204462",
            "https://www.camara.leg.br/deputados/178928",
            "https://www.camara.leg.br/deputados/178939",
            "https://www.camara.leg.br/deputados/204459",
            "https://www.camara.leg.br/deputados/81297",
            "https://www.camara.leg.br/deputados/204434",
            "https://www.camara.leg.br/deputados/178994",
            "https://www.camara.leg.br/deputados/204421",
            "https://www.camara.leg.br/deputados/178989",
            "https://www.camara.leg.br/deputados/204525",
            "https://www.camara.leg.br/deputados/178945",
            "https://www.camara.leg.br/deputados/204357",
            "https://www.camara.leg.br/deputados/204535",
            "https://www.camara.leg.br/deputados/178961",
            "https://www.camara.leg.br/deputados/204360",
            "https://www.camara.leg.br/deputados/178946",
            "https://www.camara.leg.br/deputados/204534",
            "https://www.camara.leg.br/deputados/204464",
            "https://www.camara.leg.br/deputados/178901",
            "https://www.camara.leg.br/deputados/204466",
            "https://www.camara.leg.br/deputados/215044",
            "https://www.camara.leg.br/deputados/74784",
            "https://www.camara.leg.br/deputados/178866",
            "https://www.camara.leg.br/deputados/166402",
            "https://www.camara.leg.br/deputados/204458",
            "https://www.camara.leg.br/deputados/204471",
            "https://www.camara.leg.br/deputados/204430",
            "https://www.camara.leg.br/deputados/74398",
            "https://www.camara.leg.br/deputados/204540",
            "https://www.camara.leg.br/deputados/178956",
            "https://www.camara.leg.br/deputados/204428",
            "https://www.camara.leg.br/deputados/204432",
            "https://www.camara.leg.br/deputados/204453",
            "https://www.camara.leg.br/deputados/66179",
            "https://www.camara.leg.br/deputados/205535",
            "https://www.camara.leg.br/deputados/204377",
            "https://www.camara.leg.br/deputados/73943",
            "https://www.camara.leg.br/deputados/204529",
            "https://www.camara.leg.br/deputados/204565",
            "https://www.camara.leg.br/deputados/160639",
            "https://www.camara.leg.br/deputados/160641",
            "https://www.camara.leg.br/deputados/204467",
            "https://www.camara.leg.br/deputados/178925",
            "https://www.camara.leg.br/deputados/74075",
            "https://www.camara.leg.br/deputados/220008",
            "https://www.camara.leg.br/deputados/160575",
            "https://www.camara.leg.br/deputados/204407",
            "https://www.camara.leg.br/deputados/204354",
            "https://www.camara.leg.br/deputados/160598",
            "https://www.camara.leg.br/deputados/178966",
            "https://www.camara.leg.br/deputados/107283",
            "https://www.camara.leg.br/deputados/198197",
            "https://www.camara.leg.br/deputados/67138",
            "https://www.camara.leg.br/deputados/74848",
            "https://www.camara.leg.br/deputados/108338",
            "https://www.camara.leg.br/deputados/178839",
            "https://www.camara.leg.br/deputados/204468",
            "https://www.camara.leg.br/deputados/204546",
            "https://www.camara.leg.br/deputados/160534",
            "https://www.camara.leg.br/deputados/178832",
            "https://www.camara.leg.br/deputados/204375",
            "https://www.camara.leg.br/deputados/139285",
            "https://www.camara.leg.br/deputados/204405",
            "https://www.camara.leg.br/deputados/204410"
        ]


class DeputadasSpider(scrapy.Spider):
    name = "deputadas"
    custom_settings = {
        'FEEDS': {
            'lista_deputadas.csv': {
                'format': 'csv'
            }
        }
    }

    def start_requests(self):
        urls = content
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        nome = response.css('ul.informacoes-deputado > li::text').get() 
        data_nascimento = response.css('ul.informacoes-deputado > li:nth-child(5)::text').get(),
        
        #Plenario
        temp = response.css('dd.list-table__definition-description::text').getall()
        presenca = []
        for n in temp:
            a = n.strip().split(" ")[0]
            presenca.append(a)
        
        presença_plenario = presenca[0]
        ausencia_plenario = presenca[2]
        ausencia_justificada_plenario = presenca[1]

        #Comissão
        presenca_comissao = presenca[3],
        ausencia_comissao = presenca[-1],
        ausencia_justificada_comissao = presenca[-2],

        #Gasto Parlamentar

        gasto_total_par = response.css("#percentualgastocotaparlamentar > tbody > tr > td:nth-child(2)::text").get(),

        temp = response.css("#gastomensalcotaparlamentar > tbody > tr > td::text").getall()

        gasto_jan_par = temp[1]
        gasto_fev_par = temp[4]
        gasto_mar_par = temp[7]
        gasto_abr_par = temp[10]
        gasto_maio_par = temp[13]
        gasto_junho_par = temp[16]
        gasto_jul_par = temp[19]
        gasto_agosto_par = temp[22]
        gasto_set_par = temp[25]
        gasto_out_par = temp[28]
        gasto_nov_par = temp[31]
        gasto_dez_par = 0
        

       #Gasto Gabinete

        gasto_total_gab = response.css("#percentualgastoverbagabinete > tbody > tr > td::text").getall()[1]
        
        temp = response.css("#gastomensalverbagabinete > tbody > tr > td::text").getall()

        gasto_jan_gab = temp[1]
        gasto_fev_gab = temp[4]
        gasto_mar_gab = temp[7]
        gasto_abr_gab = temp[10]
        gasto_maio_gab = temp[13]
        gasto_junho_gab = temp[16]
        gasto_jul_gab = temp[19]
        gasto_agosto_gab = temp[22]
        gasto_set_gab = temp[25]
        gasto_out_gab = temp[28]
        gasto_nov_gab = 0
        gasto_dez_gab = 0

        salario_bruto = response.css("ul.recursos-beneficios-deputado-container > li:nth-child(2) > div.beneficio > a::text").get().split(" ")[-1]


        quant_viagem = response.css("ul.recursos-beneficios-deputado-container > li:nth-child(5) > div > a::text").get()

        yield {
            'nome': nome,
            'genero': 'F', 
            'presença_plenario': presença_plenario, 
            'ausencia_plenario': ausencia_plenario,
            'ausencia_justificada_plenario': ausencia_justificada_plenario, 
            'presenca_comissao': presenca_comissao,
            'ausencia_comissao': ausencia_comissao,
            'ausencia_justificada_comissao': ausencia_justificada_comissao,
            'data_nascimento': data_nascimento,
            'gasto_total_par': gasto_total_par,
            'gasto_jan_par': gasto_jan_par,
            'gasto_fev_par': gasto_fev_par,
            'gasto_mar_par': gasto_mar_par,
            'gasto_abr_par': gasto_abr_par,
            'gasto_maio_par': gasto_maio_par,
            'gasto_junho_par': gasto_junho_par,
            'gasto_jul_par': gasto_jul_par,
            'gasto_agosto_par': gasto_agosto_par,
            'gasto_set_par': gasto_set_par,
            'gasto_out_par': gasto_out_par,
            'gasto_nov_par': gasto_nov_par,
            'gasto_dez_par': gasto_dez_par,
            'gasto_total_gab': gasto_total_gab,
            'gasto_jan_gab': gasto_jan_gab,
            'gasto_fev_gab': gasto_fev_gab,
            'gasto_mar_gab': gasto_mar_gab,
            'gasto_abr_gab': gasto_abr_gab,
            'gasto_maio_gab': gasto_maio_gab,
            'gasto_junho_gab': gasto_junho_gab,
            'gasto_jul_gab': gasto_jul_gab,
            'gasto_agosto_gab': gasto_agosto_gab,
            'gasto_set_gab': gasto_set_gab,
            'gasto_out_gab': gasto_out_gab,
            'gasto_nov_gab': gasto_nov_gab,
            'gasto_dez_gab': gasto_dez_gab,
            'salario_bruto': salario_bruto,
            'quant_viagem': quant_viagem
        }