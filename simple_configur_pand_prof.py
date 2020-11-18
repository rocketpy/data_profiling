report = pandas_profiling.ProfileReport(df,
                                        check_recoded=False,
                                        check_correlation_pearson=False,
                                        check_correlation_cramers=False,
                                        missing_diagrams={'bar': False,
                                                          'matrix': False,
                                                          'heatmap': False,
                                                          'dendrogram': False
                                                           }
                                        )
