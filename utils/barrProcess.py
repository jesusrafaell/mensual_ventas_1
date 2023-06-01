class Barr:
  def barrProcess (seg, total, long): 
    porcent = seg / total
    completed = int( porcent * long)
    rest = long - completed
    barr = f"[{'#' * completed}{'·' * rest}{porcent:.2%}]"
    return barr