import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Company, Vacancy} from "./models";
import {Observable} from "rxjs";

@Injectable({
  providedIn: 'root'
})
export class CompanyService {

  BASE_URL = "http://127.0.0.1:8000/api/companies/"
  constructor(private client: HttpClient) { }

  getCompanies(): Observable<Company[]>{
    return this.client.get<Company[]> (
      `${this.BASE_URL}`
    )
  }
  postCompany(compName: string, compDescr: string, compCity: string, compAddress: string): Observable<Company> {
    return this.client.post<Company> (
      `${this.BASE_URL}`,
      {name: compName, description: compAddress, city: compCity, address: compAddress}
    )
  }


  getCompany(comp_id: number): Observable<Company>{
    return this.client.get<Company> (
      `${this.BASE_URL}${comp_id}/`
    )
  }
  putCompany(comp_id: number,
             compName: string,
             compDescr: string,
             compCity: string,
             compAddress: string) : Observable<Company>{
    return this.client.put<Company>(
      `${this.BASE_URL}${comp_id}/`,
      {name: compName, description: compAddress, city: compCity, address: compAddress}
    )
  }
  deleteCompany(comp_id: number) : Observable<any> {
    return this.client.delete(
      `${this.BASE_URL}${comp_id}/`
    )
  }

  getCompanyVacancies(comp_id: number) : Observable<Vacancy[]>{
    return this.client.get<Vacancy[]> (
      `${this.BASE_URL}${comp_id}/vacancies`
    )
  }


}
