import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";
import {Company, Vacancy} from "./models";

@Injectable({
  providedIn: 'root'
})
export class VacancyService {
  BASE_URL = "http://127.0.0.1:8000/api/vacancies/"

  constructor(private client: HttpClient) { }

  getVacancies(): Observable<Vacancy[]> {
    return this.client.get<Vacancy[]> (
      `${this.BASE_URL}`
    )
  }

  postVacancy(vacName: string,
              vacDescr: string,
              vacSalary: number,
              vacCompany: Company): Observable<Vacancy> {
    return this.client.post<Vacancy>(
      `${this.BASE_URL}`,
      {name: vacName, description: vacDescr,
        salary: vacSalary, company: vacCompany}
    )
  }

  getVacancy(vac_id: number): Observable<Vacancy>{
    return this.client.get<Vacancy> (
      `${this.BASE_URL}${vac_id}/`
    )
  }
  putVacancy(vac_id: number,
             vacName: string,
             vacDescr: string,
             vacSalary: number,
             vacCompany: Company) : Observable<Vacancy>{
    return this.client.put<Vacancy>(
      `${this.BASE_URL}${vac_id}/`,
      {name: vacName, description: vacDescr,
        salary: vacSalary, company: vacCompany}
    )
  }
  deleteVacancy(vac_id: number): Observable<any> {
    return this.client.delete(
      `${this.BASE_URL}${vac_id}`
    )
  }

  getTopTenVacancies(): Observable<Vacancy[]> {
    return this.client.get<Vacancy[]> (
      `${this.BASE_URL}top_ten/`
    )
  }

}
