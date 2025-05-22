
select * from data_contract dc left join product_port pp on dc.port_id=pp.id left join data_product dp on pp.data_product_id=dp.id;

