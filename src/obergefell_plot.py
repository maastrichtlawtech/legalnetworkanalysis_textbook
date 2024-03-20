# for record purposes only
# pydot is deprecated and a replacement may be needed if this is to be done again
#!pip install pydot

g_ob = load_graph_from_json("data/obergefell.json")
fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(12,12))
pos = graphviz_layout(g_ob, 'dot')
nx.draw_networkx_nodes(g_ob, pos=pos, node_color='lightblue', ax=ax)
nx.draw_networkx_edges(g_ob, pos=pos, ax=ax)
nx.draw_networkx_labels(g_ob, pos=pos, labels= {"Obergefell_v_Hodges": "Obergefell", 
                                                "Loving_v_Virginia":"Loving", 
                                                "NAACP_v_State_of_Alabama":"NAACPvAlb",
                                               "Union_Pacific_Railroad_v_Botsford":"Botsford",
                                               "Lochner_v_New_York":"Lochner",
                                               "Griswold_v_Connecticut":"Griswold",
                                               "Roe_v_Wade":"Roe",
                                               "PPvCasey":"Casey",
                                               "Lawrence_v_Texas":"Lawrence",
                                               "Zablocki_v_Redhail":"Zablocki",
                                               "Baker_v_Nelson":"Baker v Nelson",
                                               "County_of_Sacramento_vs._Lewis":"CSacramentoLewis",
                                               "Romer_v_Evans":"Romer",
                                               "Bowers_v_Hardwick":"Bowers",
                                               "Turner_v_Safley":"Turner",
                                               "Windsor_v_United_States":"Windsor"}, ax=ax);
plt.savefig("images/ch3/obergefell.png")