export interface PostModel{
    text: string;
    slug: string;
    created_at: string;
    author_details: {
        username: string;
        picture: string;
    }
}

export interface PostCreationModel{
    text: string
}