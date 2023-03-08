import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";
import {Album} from "./models";
import {AlbumsComponent} from "./albums/albums.component";

@Injectable({
  providedIn: 'root'
})
export class AlbumService {
  BASE_URL: string = "https://jsonplaceholder.typicode.com";
  constructor(private client: HttpClient) {
  }

  // read albums
  getAlbums() : Observable<Album[]>{
    return this.client.get<Album[]>(`${this.BASE_URL}/albums`);
  }

  // read album
  getAlbum(id: number) : Observable<Album> {
    return this.client.get<Album>(`${this.BASE_URL}/albums/${id}`);
  }

  // create album
  addAlbum(album: Album) : Observable<Album> {
    return this.client.post<Album>(`${this.BASE_URL}/albums`, album);
  }

  // delete album
  deleteAlbum(id: number) : Observable<Album> {
    return this.client.delete<Album>(`${this.BASE_URL}/albums/${id}`);
  }
  deleteAlbum2(id: number){
    fetch('https://jsonplaceholder.typicode.com/posts/'+id, {method: 'DELETE'}).then();
  }



  // update album

}