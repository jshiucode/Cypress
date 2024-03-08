
    # -a crossing (SHARED OVER):
    if (inspected_crossing.over == crossing.under) and inspected_crossing.order_over < crossing.order_under:
        # if crossing goes through to other edge, both inspected crossing and through crossing disappear
        for through_crossing in crossing_data_for_knots:
                if through_crossing.over == crossing.over and through_crossing.order_over > crossing.order_over:
                    # make both through_crossing and inspected crossing 0 in crossing_data_for_links
                    crossing_data_for_links = edit_crossing_data_for_links(crossing_data_for_links, through_crossing.over[0], through_crossing.over[1], through_crossing.under[0], through_crossing.under[1], 0)
                    crossing_data_for_links = edit_crossing_data_for_links(crossing_data_for_links, inspected_crossing.over[0], inspected_crossing.over[1], inspected_crossing.under[0], inspected_crossing.under[1], 0)
                    return crossing_data_for_links

                if through_crossing.under == crossing.over and through_crossing.order_under > crossing.order_over:
                    # make both through_crossing and inspected crossing 0 in crossing_data_for_links
                    crossing_data_for_links = edit_crossing_data_for_links(crossing_data_for_links, through_crossing.over[0], through_crossing.over[1], through_crossing.under[0], through_crossing.under[1], 0)
                    crossing_data_for_links = edit_crossing_data_for_links(crossing_data_for_links, inspected_crossing.over[0], inspected_crossing.over[1], inspected_crossing.under[0], inspected_crossing.under[1], 0)
                    return crossing_data_for_links

        # change crossing_data_for_links accordingly (not special through case)
        # inspected crossing's over goes from (a,b) to (a,d)
        crossing_data_for_links = edit_crossing_data_for_links(crossing_data_for_links, crossing.under[0], crossing.over[1], inspected_crossing.under[0], inspected_crossing.under[1], inspected_crossing.sign)

    # -a crossing (SHARED UNDER):
    if (inspected_crossing.under == crossing.under) and inspected_crossing.order_under < crossing.order_under:
        # if crossing goes through to other edge, both inspected crossing and through crossing disappear
        for through_crossing in crossing_data_for_knots:
                if through_crossing.over == crossing.over and through_crossing.order_over > crossing.order_over:
                    # make both through_crossing and inspected crossing 0 in crossing_data_for_links
                    crossing_data_for_links = edit_crossing_data_for_links(crossing_data_for_links, through_crossing.over[0], through_crossing.over[1], through_crossing.under[0], through_crossing.under[1], 0)
                    crossing_data_for_links = edit_crossing_data_for_links(crossing_data_for_links, inspected_crossing.over[0], inspected_crossing.over[1], inspected_crossing.under[0], inspected_crossing.under[1], 0)
                    return crossing_data_for_links

                if through_crossing.under == crossing.over and through_crossing.order_under > crossing.order_over:
                    # make both through_crossing and inspected crossing 0 in crossing_data_for_links
                    crossing_data_for_links = edit_crossing_data_for_links(crossing_data_for_links, through_crossing.over[0], through_crossing.over[1], through_crossing.under[0], through_crossing.under[1], 0)
                    crossing_data_for_links = edit_crossing_data_for_links(crossing_data_for_links, inspected_crossing.over[0], inspected_crossing.over[1], inspected_crossing.under[0], inspected_crossing.under[1], 0)
                    return crossing_data_for_links

        # change crossing_data_for_links accordingly (not special through case)
        # inspected crossing's under goes from (a,b) to (a,d)
        crossing_data_for_links = edit_crossing_data_for_links(crossing_data_for_links, inspected_crossing.over[0], inspected_crossing.over[1], crossing.under[0], crossing.over[1], inspected_crossing.sign)
        # change crossing_data_for_links accordingly (not special through case)

    # -b crossing (SHARED OVER):
    if (inspected_crossing.over == crossing.under) and inspected_crossing.order_over > crossing.order_under:
        # if crossing goes through to other edge, both inspected crossing and through crossing disappear
        for through_crossing in crossing_data_for_knots:
                if through_crossing.over == crossing.over and through_crossing.order_over < crossing.order_over:
                    # make both through_crossing and inspected crossing 0 in crossing_data_for_links
                    crossing_data_for_links = edit_crossing_data_for_links(crossing_data_for_links, through_crossing.over[0], through_crossing.over[1], through_crossing.under[0], through_crossing.under[1], 0)
                    crossing_data_for_links = edit_crossing_data_for_links(crossing_data_for_links, inspected_crossing.over[0], inspected_crossing.over[1], inspected_crossing.under[0], inspected_crossing.under[1], 0)
                    return crossing_data_for_links

                if through_crossing.under == crossing.over and through_crossing.order_under < crossing.order_over:
                    # make both through_crossing and inspected crossing 0 in crossing_data_for_links
                    crossing_data_for_links = edit_crossing_data_for_links(crossing_data_for_links, through_crossing.over[0], through_crossing.over[1], through_crossing.under[0], through_crossing.under[1], 0)
                    crossing_data_for_links = edit_crossing_data_for_links(crossing_data_for_links, inspected_crossing.over[0], inspected_crossing.over[1], inspected_crossing.under[0], inspected_crossing.under[1], 0)
                    return crossing_data_for_links

        # change crossing_data_for_links accordingly (not special through case)
        # inspected crossing's over goes from (a,b) to (c,b)
        crossing_data_for_links = edit_crossing_data_for_links(crossing_data_for_links, crossing.over[0], crossing.under[1], inspected_crossing.under[0], inspected_crossing.under[1], inspected_crossing.sign)

    # -b crossing (SHARED UNDER):
    if (inspected_crossing.under == crossing.under) and inspected_crossing.order_under > crossing.order_under:
        # if crossing goes through to other edge, both inspected crossing and through crossing disappear
        for through_crossing in crossing_data_for_knots:
                if through_crossing.over == crossing.over and through_crossing.order_over < crossing.order_over:
                    # make both through_crossing and inspected crossing 0 in crossing_data_for_links
                    crossing_data_for_links = edit_crossing_data_for_links(crossing_data_for_links, through_crossing.over[0], through_crossing.over[1], through_crossing.under[0], through_crossing.under[1], 0)
                    crossing_data_for_links = edit_crossing_data_for_links(crossing_data_for_links, inspected_crossing.over[0], inspected_crossing.over[1], inspected_crossing.under[0], inspected_crossing.under[1], 0)
                    return crossing_data_for_links

                if through_crossing.under == crossing.over and through_crossing.order_under < crossing.order_over:
                    # make both through_crossing and inspected crossing 0 in crossing_data_for_links
                    crossing_data_for_links = edit_crossing_data_for_links(crossing_data_for_links, through_crossing.over[0], through_crossing.over[1], through_crossing.under[0], through_crossing.under[1], 0)
                    crossing_data_for_links = edit_crossing_data_for_links(crossing_data_for_links, inspected_crossing.over[0], inspected_crossing.over[1], inspected_crossing.under[0], inspected_crossing.under[1], 0)
                    return crossing_data_for_links

        # change crossing_data_for_links accordingly (not special through case)
        # inspected crossing's under goes from (a,b) to (c,b)
        crossing_data_for_links = edit_crossing_data_for_links(crossing_data_for_links, inspected_crossing.over[0], inspected_crossing.over[1], crossing.over[0], crossing.under[1], inspected_crossing.sign)


    # -c crossing (SHARED OVER):
    if (inspected_crossing.over == crossing.over) and inspected_crossing.order_over < crossing.order_over:
        # if crossing goes through to other edge, both inspected crossing and through crossing disappear
        for through_crossing in crossing_data_for_knots:
                if through_crossing.over == crossing.under and through_crossing.order_over > crossing.order_under:
                    # make both through_crossing and inspected crossing 0 in crossing_data_for_links
                    crossing_data_for_links = edit_crossing_data_for_links(crossing_data_for_links, through_crossing.over[0], through_crossing.over[1], through_crossing.under[0], through_crossing.under[1], 0)
                    crossing_data_for_links = edit_crossing_data_for_links(crossing_data_for_links, inspected_crossing.over[0], inspected_crossing.over[1], inspected_crossing.under[0], inspected_crossing.under[1], 0)
                    return crossing_data_for_links

                if through_crossing.under == crossing.under and through_crossing.order_under > crossing.order_under:
                    # make both through_crossing and inspected crossing 0 in crossing_data_for_links
                    crossing_data_for_links = edit_crossing_data_for_links(crossing_data_for_links, through_crossing.over[0], through_crossing.over[1], through_crossing.under[0], through_crossing.under[1], 0)
                    crossing_data_for_links = edit_crossing_data_for_links(crossing_data_for_links, inspected_crossing.over[0], inspected_crossing.over[1], inspected_crossing.under[0], inspected_crossing.under[1], 0)
                    return crossing_data_for_links

        # change crossing_data_for_links accordingly (not special through case)
        # inspected crossing's over goes from (c,d) to (c,b)
        crossing_data_for_links = edit_crossing_data_for_links(crossing_data_for_links, crossing.over[0], crossing.under[1], inspected_crossing.under[0], inspected_crossing.under[1], inspected_crossing.sign)

    # -c crossing (SHARED UNDER):
    if (inspected_crossing.under == crossing.over) and inspected_crossing.order_over > crossing.order_over:
        print("HERE")
        # if crossing goes through to other edge, both inspected crossing and through crossing disappear
        for through_crossing in crossing_data_for_knots:
                if through_crossing.over == crossing.under and through_crossing.order_over > crossing.order_under:
                    # make both through_crossing and inspected crossing 0 in crossing_data_for_links
                    crossing_data_for_links = edit_crossing_data_for_links(crossing_data_for_links, through_crossing.over[0], through_crossing.over[1], through_crossing.under[0], through_crossing.under[1], 0)
                    crossing_data_for_links = edit_crossing_data_for_links(crossing_data_for_links, inspected_crossing.over[0], inspected_crossing.over[1], inspected_crossing.under[0], inspected_crossing.under[1], 0)
                    return crossing_data_for_links

                if through_crossing.under == crossing.under and through_crossing.order_under > crossing.order_under:
                    # make both through_crossing and inspected crossing 0 in crossing_data_for_links
                    crossing_data_for_links = edit_crossing_data_for_links(crossing_data_for_links, through_crossing.over[0], through_crossing.over[1], through_crossing.under[0], through_crossing.under[1], 0)
                    crossing_data_for_links = edit_crossing_data_for_links(crossing_data_for_links, inspected_crossing.over[0], inspected_crossing.over[1], inspected_crossing.under[0], inspected_crossing.under[1], 0)
                    return crossing_data_for_links

        # change crossing_data_for_links accordingly (not special through case)
        # inspected crossing's under goes from (c,d) to (c,b)
        crossing_data_for_links = edit_crossing_data_for_links(crossing_data_for_links, inspected_crossing.over[0], inspected_crossing.over[1], crossing.over[0], crossing.under[1], inspected_crossing.sign)


    # -d crossing (SHARED OVER):
    if (inspected_crossing.over == crossing.over) and inspected_crossing.order_over > crossing.order_over:
        # if crossing goes through to other edge, both inspected crossing and through crossing disappear
        for through_crossing in crossing_data_for_knots:
                if through_crossing.over == crossing.under and through_crossing.order_over < crossing.order_under:
                    # make both through_crossing and inspected crossing 0 in crossing_data_for_links
                    crossing_data_for_links = edit_crossing_data_for_links(crossing_data_for_links, through_crossing.over[0], through_crossing.over[1], through_crossing.under[0], through_crossing.under[1], 0)
                    crossing_data_for_links = edit_crossing_data_for_links(crossing_data_for_links, inspected_crossing.over[0], inspected_crossing.over[1], inspected_crossing.under[0], inspected_crossing.under[1], 0)
                    return crossing_data_for_links

                if through_crossing.under == crossing.under and through_crossing.order_under < crossing.order_under:
                    # make both through_crossing and inspected crossing 0 in crossing_data_for_links
                    crossing_data_for_links = edit_crossing_data_for_links(crossing_data_for_links, through_crossing.over[0], through_crossing.over[1], through_crossing.under[0], through_crossing.under[1], 0)
                    crossing_data_for_links = edit_crossing_data_for_links(crossing_data_for_links, inspected_crossing.over[0], inspected_crossing.over[1], inspected_crossing.under[0], inspected_crossing.under[1], 0)
                    return crossing_data_for_links

        # change crossing_data_for_links accordingly (not special through case)
        # inspected crossing's over goes from (c,d) to (a,d)
        crossing_data_for_links = edit_crossing_data_for_links(crossing_data_for_links, crossing.under[0], crossing.over[1], inspected_crossing.under[0], inspected_crossing.under[1], inspected_crossing.sign)

    # -d crossing (SHARED UNDER):
    if (inspected_crossing.under == crossing.over) and inspected_crossing.order_over > crossing.order_over:
        # if crossing goes through to other edge, both inspected crossing and through crossing disappear
        for through_crossing in crossing_data_for_knots:
                if through_crossing.over == crossing.under and through_crossing.order_over < crossing.order_under:
                    # make both through_crossing and inspected crossing 0 in crossing_data_for_links
                    crossing_data_for_links = edit_crossing_data_for_links(crossing_data_for_links, through_crossing.over[0], through_crossing.over[1], through_crossing.under[0], through_crossing.under[1], 0)
                    crossing_data_for_links = edit_crossing_data_for_links(crossing_data_for_links, inspected_crossing.over[0], inspected_crossing.over[1], inspected_crossing.under[0], inspected_crossing.under[1], 0)
                    return crossing_data_for_links

                if through_crossing.under == crossing.under and through_crossing.order_under < crossing.order_under:
                    # make both through_crossing and inspected crossing 0 in crossing_data_for_links
                    crossing_data_for_links = edit_crossing_data_for_links(crossing_data_for_links, through_crossing.over[0], through_crossing.over[1], through_crossing.under[0], through_crossing.under[1], 0)
                    crossing_data_for_links = edit_crossing_data_for_links(crossing_data_for_links, inspected_crossing.over[0], inspected_crossing.over[1], inspected_crossing.under[0], inspected_crossing.under[1], 0)
                    return crossing_data_for_links

        # change crossing_data_for_links accordingly (not special through case)
        # inspected crossing's under goes from (c,d) to (a,d)
        crossing_data_for_links = edit_crossing_data_for_links(crossing_data_for_links, inspected_crossing.over[0], inspected_crossing.over[1], crossing.under[0], crossing.over[1], inspected_crossing.sign)





    return crossing_data_for_links